import hashlib

routes_patches = {
    'INICIO':  'index.html',
    'REGISTRO_EXITOSO': 'register_success.html'
}

API_METHOD= 'only post'

def hash_password(password):
    password_bytes = password.encode('utf-8')
    
    sha256_hash = hashlib.sha256(password_bytes)
    
    hashed_password = sha256_hash.hexdigest()
    
    return hashed_password