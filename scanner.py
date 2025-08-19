# Import library socket bawaan Python, dipakai untuk komunikasi jaringan
import socket  

# Fungsi untuk memindai 1 port pada 1 alamat IP
def scan_port(ip, port):
    # Membuat objek socket: AF_INET = IPv4, SOCK_STREAM = TCP
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set timeout 1 detik supaya tidak terlalu lama menunggu respon
    scanner.settimeout(1)

    try:
        # Mencoba koneksi ke (ip, port)
        scanner.connect((ip, port))

        # Kalau berhasil → artinya port terbuka
        print(f"[+] Port {port} terbuka")

        # Tutup koneksi biar tidak menggantung
        scanner.close()

    except:
        # Kalau gagal (port tertutup / tidak bisa diakses), biarkan saja
        pass


# Fungsi utama program
def main():
    # Meminta input dari user (alamat IP target)
    target = input("Masukkan IP target: ")

    # Loop dari port 1 sampai 1024
    # range(1, 1025) = mulai dari 1, berhenti sebelum 1025 → jadi 1-1024
    for port in range(1, 1025):
        scan_port(target, port)


# Bagian ini memastikan program hanya dijalankan
# kalau file ini di-run langsung, bukan di-import
if __name__ == "__main__":
    main()
