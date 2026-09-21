import os
import subprocess
import shutil

project_dir = r"D:\TOAN\ppt-master\projects\bai1_toan12_don_dieu_cuc_tri_20260921"
tikz_dir = os.path.join(project_dir, "tikz")
slide_bai_giang_tikz = r"D:\TOAN\SLIDE BAI GIANG\tikz_bai1_toan12"
img_out_dir = os.path.join(project_dir, "images")

os.makedirs(tikz_dir, exist_ok=True)
os.makedirs(slide_bai_giang_tikz, exist_ok=True)
os.makedirs(img_out_dir, exist_ok=True)

def make_tikz_doc(body):
    return r'''\documentclass[tikz,border=5mm]{standalone}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage{tkz-tab}
\usetikzlibrary{calc,shapes,backgrounds,arrows.meta,patterns}

\definecolor{slate}{RGB}{100,116,139}

\begin{document}
''' + body + r'''
\end{document}
'''

# 1. Đồ thị HĐ1 và VD1 (y = x^2 và y = |x|)
tikz_01 = make_tikz_doc(r'''
\begin{tikzpicture}[>=stealth,line join=round,line cap=round,scale=0.9,font=\large]
  % Do thi y = x^2
  \begin{scope}[shift={(-4.2,0)}]
    \node[font=\bfseries\Large, text=blue!80!black] at (0, 3.5) {ĐỒ THỊ $y = x^2$ (HĐ1)};
    \draw[->, thick] (-2.5,0) -- (2.8,0) node[below] {$x$};
    \draw[->, thick] (0,-0.8) -- (0,3.3) node[left] {$y$};
    \node[below left] at (0,0) {$O$};
    \draw[very thick, blue!80!black, smooth, domain=-1.7:1.7] plot (\x, {(\x)^2});
    \node[font=\bfseries, text=red!80!black] at (-1.5, -1.3) {$(-\infty; 0)$: Đi xuống};
    \node[font=\bfseries, text=blue!80!black] at (1.5, -1.3) {$(0; +\infty)$: Đi lên};
  \end{scope}

  % Do thi y = |x| (VD1)
  \begin{scope}[shift={(4.2,0)}]
    \node[font=\bfseries\Large, text=green!60!black] at (0, 3.5) {ĐỒ THỊ $y = |x|$ (VD1)};
    \draw[->, thick] (-2.5,0) -- (2.8,0) node[below] {$x$};
    \draw[->, thick] (0,-0.8) -- (0,3.3) node[left] {$y$};
    \node[below left] at (0,0) {$O$};
    \draw[very thick, green!60!black] (-2,2) -- (0,0) -- (2,2);
    \node[font=\bfseries, text=red!80!black] at (-1.5, -1.3) {$(-\infty; 0)$: Nghịch biến};
    \node[font=\bfseries, text=green!60!black] at (1.5, -1.3) {$(0; +\infty)$: Đồng biến};
  \end{scope}
\end{tikzpicture}
''')

# 2. Đồ thị LT1 (Hàm bậc 3 đổi chiều)
tikz_02 = make_tikz_doc(r'''
\begin{tikzpicture}[>=stealth,line join=round,line cap=round,scale=1.0,font=\large]
  \node[font=\bfseries\Large, text=blue!80!black] at (0, 3.6) {ĐỒ THỊ LUYỆN TẬP 1 (HÌNH 1.5 SGK)};
  \draw[->, thick] (-3,0) -- (3.5,0) node[below] {$x$};
  \draw[->, thick] (0,-2.5) -- (0,3.2) node[left] {$y$};
  \node[below left] at (0,0) {$O$};

  % Do thi y = x^3 - 3x
  \draw[very thick, purple!80!black, smooth, domain=-2.1:2.1] plot (\x, {0.8*((\x)^3 - 3*(\x))});

  \draw[dashed, gray] (-1,0) node[below=2pt, text=black] {$-1$} -- (-1, 1.6) -- (0, 1.6) node[left=2pt, text=black] {$2$};
  \draw[dashed, gray] (1,0) node[above=2pt, text=black] {$1$} -- (1, -1.6) -- (0, -1.6) node[right=2pt, text=black] {$-2$};
  \fill[purple!90!black] (-1, 1.6) circle (2.5pt);
  \fill[purple!90!black] (1, -1.6) circle (2.5pt);

  \node[font=\bfseries, text=blue!80!black] at (-2.2, 2.5) {Đồng biến};
  \node[font=\bfseries, text=red!80!black] at (0, 0.5) {Nghịch biến};
  \node[font=\bfseries, text=blue!80!black] at (2.2, -2.2) {Đồng biến};
\end{tikzpicture}
''')

# 3. BBT VD3: y = -x^3 + 3x^2 - 1
tikz_03 = make_tikz_doc(r'''
\begin{tikzpicture}[font=\large]
  \tkzTabInit[lgt=2.0,espcl=2.8,deltacl=0.8]
  {$x$ /1.0, $y'$ /1.0, $y$ /2.2}
  {$-\infty$, $0$, $2$, $+\infty$}
  \tkzTabLine{,-,0,+,0,-,}
  \tkzTabVar{+/ $+\infty$, -/ $-1$, +/ $3$, -/ $-\infty$}
\end{tikzpicture}
''')

# 4. BBT VD4: y = (x - 1)/(x + 1)
tikz_04 = make_tikz_doc(r'''
\begin{tikzpicture}[font=\large]
  \tkzTabInit[lgt=2.0,espcl=3.2,deltacl=0.8]
  {$x$ /1.0, $y'$ /1.0, $y$ /2.2}
  {$-\infty$, $-1$, $+\infty$}
  \tkzTabLine{,+,d,+,}
  \tkzTabVar{-/ $1$, +d/ $+\infty$ / $-\infty$, +/ $1$}
\end{tikzpicture}
''')

# 5. Đồ thị cực trị VD5 & LT4
tikz_05 = make_tikz_doc(r'''
\begin{tikzpicture}[>=stealth,line join=round,line cap=round,scale=1.1,font=\large]
  \draw[->, thick] (-2.2,0) -- (3.5,0) node[below] {$x$};
  \draw[->, thick] (0,-2.2) -- (0,3.5) node[left] {$y$};
  \node[below left] at (0,0) {$O$};

  \draw[very thick, blue!80!black, smooth, domain=-2.1:2.3] plot (\x, {0.6*((\x)^3 - 3*(\x)) + 1});

  % Diem Cuc Dai
  \coordinate (A) at (-1, 2.2);
  \draw[dashed, gray] (-1,0) node[below, text=black, font=\bfseries] {$x_{CĐ} = -1$} -- (A) -- (0,2.2) node[left, text=black, font=\bfseries] {$y_{CĐ} = 2$};
  \fill[blue!90!black] (A) circle (3pt) node[above=4pt, text=blue!90!black, font=\bfseries] {Cực Đại $A(-1; 2)$};
  \draw[thick, blue!80!black, <->] (-1.8, 2.2) -- (-0.2, 2.2);

  % Diem Cuc Tieu
  \coordinate (B) at (1, -0.2);
  \draw[dashed, gray] (1,0) node[above=4pt, text=black, font=\bfseries] {$x_{CT} = 1$} -- (B) -- (0,-0.2) node[left, text=black, font=\bfseries] {$y_{CT} = -2$};
  \fill[red!90!black] (B) circle (3pt) node[below=6pt, text=red!90!black, font=\bfseries] {Cực Tiểu $B(1; -2)$};
  \draw[thick, red!80!black, <->] (0.2, -0.2) -- (1.8, -0.2);
\end{tikzpicture}
''')

# 6. Bảng quy tắc đổi dấu đạo hàm
tikz_06 = make_tikz_doc(r'''
\begin{tikzpicture}[font=\large]
  % Cuc dai
  \begin{scope}[shift={(-4.5,0)}]
    \node[font=\bfseries\Large, text=blue!90!black] at (2.2, 2.6) {ĐỔI DẤU $(+) \to (-)$: CỰC ĐẠI};
    \tkzTabInit[lgt=1.8,espcl=2.2,deltacl=0.6]
    {$x$ /0.9, $f'(x)$ /0.9, $f(x)$ /1.8}
    {$x_0 - h$, $x_0$, $x_0 + h$}
    \tkzTabLine{,+,0,-,}
    \tkzTabVar{-/ , +/ $f(x_0)$ (Cực đại), -/ }
  \end{scope}

  % Cuc tieu
  \begin{scope}[shift={(4.5,0)}]
    \node[font=\bfseries\Large, text=red!90!black] at (2.2, 2.6) {ĐỔI DẤU $(-) \to (+)$: CỰC TIỂU};
    \tkzTabInit[lgt=1.8,espcl=2.2,deltacl=0.6]
    {$x$ /0.9, $f'(x)$ /0.9, $f(x)$ /1.8}
    {$x_0 - h$, $x_0$, $x_0 + h$}
    \tkzTabLine{,-,0,+,}
    \tkzTabVar{+/ , -/ $f(x_0)$ (Cực tiểu), +/ }
  \end{scope}
\end{tikzpicture}
''')

# 7. BBT VD6: y = 2x^3 - 9x^2 + 12x - 3
tikz_07 = make_tikz_doc(r'''
\begin{tikzpicture}[font=\large]
  \tkzTabInit[lgt=2.0,espcl=2.8,deltacl=0.8]
  {$x$ /1.0, $y'$ /1.0, $y$ /2.2}
  {$-\infty$, $1$, $2$, $+\infty$}
  \tkzTabLine{,+,0,-,0,+,}
  \tkzTabVar{-/ $-\infty$, +/ $2$, -/ $1$, +/ $+\infty$}
\end{tikzpicture}
''')

# 8. BBT VD7: y = x^4 - 2x^2 + 2
tikz_08 = make_tikz_doc(r'''
\begin{tikzpicture}[font=\large]
  \tkzTabInit[lgt=2.0,espcl=2.4,deltacl=0.6]
  {$x$ /1.0, $y'$ /1.0, $y$ /2.2}
  {$-\infty$, $-1$, $0$, $1$, $+\infty$}
  \tkzTabLine{,-,0,+,0,-,0,+,}
  \tkzTabVar{+/ $+\infty$, -/ $1$, +/ $2$, -/ $1$, +/ $+\infty$}
\end{tikzpicture}
''')

# 9. Vận dụng 2: Phóng vật h(t) = 1 + 10t - 5t^2
tikz_09 = make_tikz_doc(r'''
\begin{tikzpicture}[>=stealth,line join=round,line cap=round,scale=1.1,font=\large]
  \draw[->, thick] (-0.5,0) -- (3.2,0) node[below] {$t\text{ (giây)}$};
  \draw[->, thick] (0,-0.5) -- (0,4.2) node[left] {$h(t)\text{ (m)}$};
  \node[below left] at (0,0) {$O$};

  % Do thi h(t) = -5(t-1)^2 + 6 tren [0; 2.1]
  \draw[very thick, teal!80!black, smooth, domain=0:2.1] plot (\x, {0.6*(-5*(\x-1)^2 + 6)});

  \coordinate (M) at (1, 3.6);
  \draw[dashed, gray] (1,0) node[below, text=black, font=\bfseries] {$t = 1$} -- (M) -- (0,3.6) node[left, text=black, font=\bfseries] {$h_{\max} = 6$};
  \fill[red!90!black] (M) circle (3pt) node[above=4pt, text=red!90!black, font=\bfseries] {Độ cao lớn nhất: $6\text{ m}$};
  \node[left] at (0, 0.6) {$1$};
  \node[below, font=\normalsize, text=gray!80!black] at (1.5, -0.8) {Vật đạt độ cao lớn nhất sau $1$ giây};
\end{tikzpicture}
''')

items = [
    ("tikz_01_dothi_hd1_vd1", tikz_01),
    ("tikz_02_dothi_lt1", tikz_02),
    ("tikz_03_bbt_vd3", tikz_03),
    ("tikz_04_bbt_vd4", tikz_04),
    ("tikz_05_dothi_cuc_tri_vd5", tikz_05),
    ("tikz_06_dinh_ly_doi_dau", tikz_06),
    ("tikz_07_bbt_vd6", tikz_07),
    ("tikz_08_bbt_vd7", tikz_08),
    ("tikz_09_van_dung_2", tikz_09),
]

for name, content in items:
    tex_path = os.path.join(tikz_dir, f"{name}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(content)
    shutil.copy(tex_path, os.path.join(slide_bai_giang_tikz, f"{name}.tex"))
    print(f"Saved TeX: {name}.tex")

    res = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", f"{name}.tex"],
        cwd=tikz_dir,
        capture_output=True,
        text=True
    )
    if res.returncode == 0:
        pdf_path = os.path.join(tikz_dir, f"{name}.pdf")
        png_prefix = os.path.join(img_out_dir, name)
        subprocess.run(
            ["pdftoppm", "-png", "-r", "600", pdf_path, png_prefix],
            capture_output=True
        )
        for f in os.listdir(img_out_dir):
            if f.startswith(name) and f.endswith(".png"):
                src_png = os.path.join(img_out_dir, f)
                dst_png = os.path.join(img_out_dir, f"{name}.png")
                dst_slide_png = os.path.join(slide_bai_giang_tikz, f"{name}.png")
                if src_png != dst_png:
                    shutil.move(src_png, dst_png)
                shutil.copy(dst_png, dst_slide_png)
                print(f"Compiled 600 DPI PNG: {name}.png")
                break
    else:
        print(f"ERROR compiling {name}:", res.stderr or res.stdout[:300])

print("All TikZ diagrams compiled successfully!")
