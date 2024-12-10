def buat_papan():
  """Membuat papan Othello awal."""
  papan = [[' ' for _ in range(8)] for _ in range(8)]
  papan[3][3] = 'W'
  papan[3][4] = 'B'
  papan[4][3] = 'B'
  papan[4][4] = 'W'
  return papan

def cetak_papan(papan):
  """Mencetak papan Othello."""
  print('  +---+---+---+---+---+---+---+---+')
  for i in range(8):
    print(i+1, end=' | ')
    for j in range(8):
      print(papan[i][j], end=' | ')
    print('\n  +---+---+---+---+---+---+---+---+')
  print('    a   b   c   d   e   f   g   h')

def gerakan_valid(papan, pemain, baris, kolom):
  """Memeriksa apakah gerakan valid."""
  if papan[baris][kolom] != ' ':
    return False

  lawan = 'B' if pemain == 'W' else 'W'
  arah = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

  for dr, dc in arah:
    r, c = baris + dr, kolom + dc
    if 0 <= r < 8 and 0 <= c < 8 and papan[r][c] == lawan:
      r += dr
      c += dc
      while 0 <= r < 8 and 0 <= c < 8 and papan[r][c] == lawan:
        r += dr
        c += dc
      if 0 <= r < 8 and 0 <= c < 8 and papan[r][c] == pemain:
        return True

  return False

def buat_gerakan(papan, pemain, baris, kolom):
  """Membuat gerakan pada papan."""
  papan[baris][kolom] = pemain

  lawan = 'B' if pemain == 'W' else 'W'
  arah = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

  for dr, dc in arah:
    r, c = baris + dr, kolom + dc
    if 0 <= r < 8 and 0 <= c < 8 and papan[r][c] == lawan:
      temp = []
      while 0 <= r < 8 and 0 <= c < 8 and papan[r][c] == lawan:
        temp.append((r, c))
        r += dr
        c += dc
      if 0 <= r < 8 and 0 <= c < 8 and papan[r][c] == pemain:
        for r, c in temp:
          papan[r][c] = pemain

def dapatkan_gerakan_valid(papan, pemain):
  """Mendapatkan semua gerakan valid."""
  gerakan = []
  for i in range(8):
    for j in range(8):
      if gerakan_valid(papan, pemain, i, j):
        gerakan.append((i, j))
  return gerakan

def hitung_skor(papan):
  """Menghitung skor."""
  skor_hitam = 0
  skor_putih = 0
  for i in range(8):
    for j in range(8):
      if papan[i][j] == 'B':
        skor_hitam += 1
      elif papan[i][j] == 'W':
        skor_putih += 1
  return skor_hitam, skor_putih

def main():
  """Fungsi utama untuk menjalankan permainan."""
  papan = buat_papan()
  pemain = 'B'  # Mulai dengan pemain Hitam

  while True:
    cetak_papan(papan)
    skor_hitam, skor_putih = hitung_skor(papan)
    print('Skor: Hitam', skor_hitam, '- Putih', skor_putih)
    gerakan = dapatkan_gerakan_valid(papan, pemain)

    if not gerakan:
      print('Pemain', pemain, 'tidak memiliki gerakan valid.')
      pemain = 'B' if pemain == 'W' else 'W'  # Ganti giliran
      gerakan = dapatkan_gerakan_valid(papan, pemain)
      if not gerakan:
        print('Permainan berakhir!')
        skor_hitam, skor_putih = hitung_skor(papan)
        print('Skor akhir: Hitam', skor_hitam, '- Putih', skor_putih)
        if skor_hitam > skor_putih:
          print('Pemain Hitam menang!')
        elif skor_putih > skor_hitam:
          print('Pemain Putih menang!')
        else:
          print('Seri!')
        break

    print('Giliran pemain', pemain)
    if pemain == 'B':
      # Giliran pemain Hitam, minta input
      while True:
        try:
          inp = input('Masukkan gerakan (contoh: d3): ')
          kolom = ord(inp[0].lower()) - ord('a')
          baris = int(inp[1]) - 1
          if (baris, kolom) in gerakan:
            break
          else:
            print('Gerakan tidak valid. Coba lagi.')
        except (ValueError, IndexError):
          print('Input tidak valid. Coba lagi.')
    else:
      # Giliran pemain Putih (komputer), pilih gerakan valid pertama
      baris, kolom = gerakan[0]
      print('Komputer memilih:', chr(kolom + ord('a')) + str(baris + 1))

    buat_gerakan(papan, pemain, baris, kolom)
    pemain = 'W' if pemain == 'B' else 'B'  # Ganti giliran


if __name__ == '__main__':
  main()