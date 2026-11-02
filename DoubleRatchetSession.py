from cryptography.hazmat.primitives.asymmetric import x25519
class DoubleRatchetSession:
    def __init__(self, initial_root_key: bytes, initial_dh_r):
        """
        Inicializa el estado criptográfico de la sesión Double Ratchet.
        """
        # 1. Clave Raíz (Root Key - RK) de 128/256 bits
        self.rk = initial_root_key
        
        # 2. Claves de Cadena (Chain Keys) para simetría
        self.ck_s = None  # Sending Chain Key
        self.ck_r = None  # Receiving Chain Key
        
        # 3. Estados Diffie-Hellman (DH Ratchet)
        self.dh_s = x25519.X25519PrivateKey.generate()  # Par propio actual (Privada, Pública)
        self.dh_r = x25519.X25519PublicKey.generate() # Clave pública actual de la contraparte
        
        # 4. Contadores de mensajes
        self.n_s = 0  # Número de mensajes enviados en la cadena actual
        self.n_r = 0  # Número de mensajes recibidos en la cadena actual
        self.pn = 0   # Número de mensajes enviados en la cadena anterior
        
        # 5. Búfer para claves de mensajes fuera de orden o saltadas
        self.mks_skipped = {}  # Diccionario: (dh_public_key, counter) -> message_key

    def symmetric_ratchet_send(self):
        """
        [Trinquete Simétrico - Salida]
        Deriva una nueva 'Message Key' a partir de la 'Sending Chain Key' (ck_s)
        y actualiza la ck_s.
        """
        # TODO: Implementar derivación HMAC/HKDF para la cadena de envío
        pass

    def symmetric_ratchet_receive(self):
        """
        [Trinquete Simétrico - Entrada]
        Deriva una nueva 'Message Key' a partir de la 'Receiving Chain Key' (ck_r)
        y actualiza la ck_r.
        """
        # TODO: Implementar derivación HMAC/HKDF para la cadena de recepción
        pass

    def dh_ratchet_step(self, remote_dh_public_key):
        """
        [Trinquete Diffie-Hellman]
        Se ejecuta al recibir una nueva clave pública DH de la otra parte.
        Actualiza la Root Key, la cadena de recepción y genera un nuevo par DH propio.
        """
        # TODO: 
        # 1. Realizar cómputo DH con la clave pública nueva de la contraparte y nuestra privada actual.
        # 2. Actualizar Root Key y Receiving Chain Key usando HKDF.
        # 3. Generar un nuevo par de claves DH propio (dh_s).
        # 4. Realizar nuevo cómputo DH con la nueva clave pública propia y la de la contraparte.
        # 5. Actualizar Root Key y Sending Chain Key usando HKDF.
        pass

    def encrypt_message(self, plaintext: bytes) -> dict:
        """
        Prepara el mensaje para ser enviado:
        - Ejecuta el trinquete simétrico para obtener la clave de mensaje.
        - Cifra el texto plano usando AES-GCM (128 bits).
        - Empaqueta las cabeceras (clave pública DH actual, n_s, pn).
        """
        # TODO: Integrar AES-GCM y armar el paquete de salida
        pass

    def decrypt_message(self, header, ciphertext: bytes, iv: bytes) -> bytes:
        """
        Procesa el mensaje entrante:
        - Verifica si hay cambio en la clave pública DH (ejecuta DH Ratchet si aplica).
        - Maneja claves saltadas si hay desorden.
        - Obtiene la clave de mensaje mediante el trinquete simétrico.
        - Descifra con AES-GCM.
        """
        # TODO: Integrar validación de cabeceras, DH Ratchet y descifrado AES-GCM
        pass