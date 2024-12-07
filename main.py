import pywhatkit as kit
import pyautogui
import time

# Daftar nomor WhatsApp (dengan kode negara, tanpa tanda +)
nomor_telepon = [
    "6287878224307"  # Pastikan format nomor benar
]

# Pesan yang akan dikirim
pesan = """
*Penawaran digiwork*

*Paket Lengkap Pembuatan Website dan Sistem Manajemen untuk Perusahaan Anda*

Digiwork Inc adalah perusahaan teknologi yang berpengalaman dalam membantu bisnis mencapai tujuan mereka melalui solusi digital. Kami menawarkan paket lengkap pembuatan website dan sistem manajemen untuk meningkatkan efisiensi dan produktivitas perusahaan Anda.

*Layanan* 
1. *Landing Page:* Desain dan pengembangan landing page yang menarik dan efektif untuk meningkatkan konversi.
2. *Sistem Manajemen Perusahaan:* Pengembangan sistem manajemen perusahaan yang terintegrasi untuk mengelola data dan proses bisnis.
3. *Sistem Absensi:* Pengembangan sistem absensi online untuk memantau kehadiran karyawan.
4. *Pengolahan Data Terorganisir:* Pengembangan sistem pengolahan data untuk mengelola dan menganalisis data perusahaan.
5. *Desain Web Responsive:* Desain website yang responsif dan kompatibel dengan perangkat mobile.
6. *Pengembangan Aplikasi:* Pengembangan aplikasi mobile dan web untuk meningkatkan pengalaman pengguna.
7. *Pemeliharaan dan Update:* Pemeliharaan dan update rutin untuk memastikan sistem tetap stabil dan aman.

*Kelebihan*
1. Tim yang berpengalaman dan profesional.
2. Teknologi terkini dan terintegrasi.
3. Desain yang menarik dan responsif.
4. Sistem yang aman dan stabil.
5. Dukungan teknis pada jam kerja.
6. Biaya yang kompetitif.

*Paket Harga*
1. *Paket Basic:* Rp 5.000.000 (landing page dan sistem manajemen dasar).
2. *Paket Standard:* Rp 10.000.000 (sistem manajemen lengkap dan sistem absensi).
3. *Paket Premium:* Rp 20.000.000 (sistem manajemen lengkap, sistem absensi, dan pengolahan data terorganisir).
4. *Paket Custom:* Harga disesuaikan dengan kebutuhan perusahaan.

*Kontak*
Hubungi kami untuk informasi lebih lanjut untuk janji bertemu atau konsultasi online:

Email: mailto:digiwork.inc@gmail.com
Telepon: 087878224307
"""

path_gambar = ("gambar.jpeg")  # Path ke file gambar

# Kirim gambar dan pesan ke setiap nomor
for nomor in nomor_telepon:
    try:
        # Kirim gambar dengan caption
        kit.sendwhats_image(receiver=f"+{nomor}", img_path=path_gambar, caption=pesan)

        # Beri jeda waktu untuk memastikan WhatsApp Web terbuka
        time.sleep(5)  # Tambahkan jeda agar sistem stabil

        # Simulasikan "Enter" untuk mengirim pesan
        pyautogui.press("enter")  # Kirim pesan di kotak input WhatsApp
        time.sleep(10)  # Jeda untuk menghindari blokir

        print(f"Gambar dan pesan terkirim ke {nomor}")
    except Exception as e:
        print(f"Gagal mengirim pesan ke {nomor}. Error: {e}")
