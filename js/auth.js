// Initialize AWS SDK
AWS.config.update({
    region: 'YOUR_AWS_REGION',
    credentials: new AWS.CognitoIdentityCredentials({
        IdentityPoolId: 'YOUR_IDENTITY_POOL_ID'
    })
});

// Tab switching
document.getElementById('loginTab').addEventListener('click', function() {
    this.classList.add('active');
    document.getElementById('signupTab').classList.remove('active');
    document.getElementById('loginForm').style.display = 'block';
    document.getElementById('signupForm').style.display = 'none';
});

document.getElementById('signupTab').addEventListener('click', function() {
    this.classList.add('active');
    document.getElementById('loginTab').classList.remove('active');
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('signupForm').style.display = 'block';
});

// Sign Up Function
async function signup() {
    const name = document.getElementById('signupName').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    
    const userPool = new AmazonCognitoIdentity.CognitoUserPool({
        UserPoolId: 'us-east-1_jz77bUPkk',
        ClientId: 'to1hm2drj7n1adfiabu9lmdnh'
    });
    
    const attributeList = [
        new AmazonCognitoIdentity.CognitoUserAttribute({
            Name: 'name',
            Value: name
        }),
        new AmazonCognitoIdentity.CognitoUserAttribute({
            Name: 'email',
            Value: email
        })
    ];
    
    try {
        const result = await new Promise((resolve, reject) => {
            userPool.signUp(email, password, attributeList, null, (err, result) => {
                if (err) reject(err);
                else resolve(result);
            });
        });
        
        alert('Registration successful! Please check your email to verify your account.');
    } catch (error) {
        console.error('Error signing up:', error);
        alert('Registration failed: ' + error.message);
    }
}

// Login Function
async function login() {
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    
    const userPool = new AmazonCognitoIdentity.CognitoUserPool({
        UserPoolId: 'us-east-1_jz77bUPkk',
        ClientId: 'to1hm2drj7n1adfiabu9lmdnh'
    });
    
    const userData = {
        Username: email,
        Pool: userPool
    };
    
    const cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
    
    const authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails({
        Username: email,
        Password: password
    });
    
    try {
        const result = await new Promise((resolve, reject) => {
            cognitoUser.authenticateUser(authenticationDetails, {
                onSuccess: resolve,
                onFailure: reject
            });
        });
        
        // Store tokens in localStorage
        localStorage.setItem('accessToken', result.getAccessToken().getJwtToken());
        localStorage.setItem('idToken', result.getIdToken().getJwtToken());
        localStorage.setItem('refreshToken', result.getRefreshToken().getToken());
        
        // Redirect to home page
        window.location.href = 'home.html';
    } catch (error) {
        console.error('Error logging in:', error);
        alert('Login failed: ' + error.message);
    }
}