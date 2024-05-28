# Interpolasi Polinom Lagrange dan Newton

Repositori ini berisi implementasi metode interpolasi polinom Lagrange dan Newton untuk menemukan hubungan antara tegangan yang diberikan kepada baja tahan-karat dan waktu yang diperlukan hingga baja tersebut patah.

## Data
Data yang digunakan merupakan hasil pengukuran hubungan antara tegangan dan waktu patah:

| Tegangan (kg/mm^2) | Waktu Patah (jam) |
|--------------------|-------------------|
| 5                  | 40                |
| 10                 | 30                |
| 15                 | 25                |
| 20                 | 40                |
| 25                 | 18                |
| 30                 | 20                |
| 35                 | 22                |
| 40                 | 15                |

## Struktur Proyek
- `lagrange_interpolation.py`: Implementasi interpolasi polinom Lagrange.
- `newton_interpolation.py`: Implementasi interpolasi polinom Newton.
- `test_interpolation.py`: Kode pengujian dan plotting hasil interpolasi.
