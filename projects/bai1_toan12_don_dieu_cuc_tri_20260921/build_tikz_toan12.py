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

# 1. Đồ thị minh họa tính đồng biến & nghịch biến
tikz_01 = make_tikz_doc(r'''
\begin{tikzpicture}[>=stealth,line join=round,line cap=round,scale=0.9,font=\large]
  % Do thi dong bien (ben trai)
  \begin{scope}[shift={(-4.2,0)}]
    \node[font=\bfseries\Large, text=blue!80!black] at (0, 3.2) {ĐỒNG BIẾN (TĂNG)};
    \draw[->, thick] (-2.5,0) -- (3,0) node[below] {$x$};
    \draw[->, thick] (0,-1.5) -- (0,3) node[left] {$y$};
    \node[below left] at (0,0) {$O$};

    % Do thi y = x^3/4 - x/2 + 0.8
    \draw[very thick, blue!80!black, smooth, domain=-2:2.2] plot (\x, {0.2*(\x)^3 + 0.3*(\x) + 0.5});
    
    % Hai diem x1 < x2
    \coordinate (X1) at (-1, 0.2);
    \coordinate (X2) at (1.5, 1.625);
    \draw[dashed, gray] (-1,0) node[below, text=black] {$x_1$} -- (-1,0.2) -- (0,0.2) node[left, text=black] {$f(x_1)$};
    \draw[dashed, gray] (1.5,0) node[below, text=black] {$x_2$} -- (1.5,1.625) -- (0,1.625) node[left, text=black] {$f(x_2)$};
    \fill[blue!90!black] (-1,0.2) circle (2.5pt);
    \fill[blue!90!black] (1.5,1.625) circle (2.5pt);

    \node[font=\bfseries, text=blue!90!black] at (0, -2.2) {$x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$};
    \node[font=\normalsize, text=gray!80!black] at (0, -2.8) {Đồ thị đi lên từ trái sang phải};
  \end{scope}

  % Do thi nghich bien (ben phai)
  \begin{scope}[shift={(4.2,0)}]
    \node[font=\bfseries\Large, text=red!80!black] at (0, 3.2) {NGHỊCH BIẾN (GIẢM)};
    \draw[->, thick] (-2.5,0) -- (3,0) node[below] {$x$};
    \draw[->, thick] (0,-1.5) -- (0,3) node[left] {$y$};
    \node[below left] at (0,0) {$O$};

    % Do thi y = -0.2*x^3 - 0.3*x + 0.5
    \draw[very thick, red!80!black, smooth, domain=-2.2:2] plot (\x, {-0.2*(\x)^3 - 0.3*(\x) + 0.5});

    % Hai diem x1 < x2
    \draw[dashed, gray] (-1.5,0) node[below, text=black] {$x_1$} -- (-1.5,1.625) -- (0,1.625) node[left, text=black] {$f(x_1)$};
    \draw[dashed, gray] (1,0) node[below, text=black] {$x_2$} -- (1,0) -- (0,0) node[right, text=black] {$f(x_2)$};
    \fill[red!90!black] (-1.5,1.625) circle (2.5pt);
    \fill[red!90!black] (1,0) circle (2.5pt);

    \node[font=\bfseries, text=red!90!black] at (0, -2.2) {$x_1 < x_2 \Rightarrow f(x_1) > f(x_2)$};
    \node[font=\normalsize, text=gray!80!black] at (0, -2.8) {Đồ thị đi xuống từ trái sang phải};
  \end{scope}
\end{tikzpicture}
''')

# 2. Bảng biến thiên xét tính đơn điệu (tkz-tab)
tikz_02 = make_tikz_doc(r'''
\begin{tikzpicture}[font=\large]
  \tkzTabInit[lgt=2.2,espcl=3.2,deltacl=0.8]
  {$x$ /1.0, $y'$ /1.0, $y$ /2.0}
  {$-\infty$, $-1$, $2$, $+\infty$}
  \tkzTabLine{,+,0,-,0,+,}
  \tkzTabVar{-/ $-\infty$, +/ $7$, -/ $-20$, +/ $+\infty$}
\end{tikzpicture}
''')

# 3. Đồ thị đỉnh đồi và đáy thung lũng (Cực đại & Cực tiểu)
tikz_03 = make_tikz_doc(r'''
\begin{tikzpicture}[>=stealth,line join=round,line cap=round,scale=1.1,font=\large]
  % Truc Oxy
  \draw[->, thick] (-2.2,0) -- (3.5,0) node[below] {$x$};
  \draw[->, thick] (0,-2.2) -- (0,3.5) node[left] {$y$};
  \node[below left] at (0,0) {$O$};

  % Do thi y = x^3 - 3x + 1
  \draw[very thick, blue!80!black, smooth, domain=-2.1:2.3] plot (\x, {0.6*((\x)^3 - 3*(\x)) + 1});

  % Diem Cuc Dai A(-1, 2.2)
  \coordinate (A) at (-1, 2.2);
  \draw[dashed, gray] (-1,0) node[below, text=black, font=\bfseries] {$x_{CĐ}$} -- (A) -- (0,2.2) node[left, text=black, font=\bfseries] {$y_{CĐ}$};
  \fill[blue!90!black] (A) circle (3pt) node[above=4pt, text=blue!90!black, font=\bfseries\Large] {Điểm Cực Đại};
  \draw[thick, blue!80!black, <->] (-1.8, 2.2) -- (-0.2, 2.2);
  \node[above, font=\footnotesize, text=gray!80!black] at (-1, 2.4) {Tiếp tuyến ngang: $y'=0$};

  % Diem Cuc Tieu B(1, -0.2)
  \coordinate (B) at (1, -0.2);
  \draw[dashed, gray] (1,0) node[above=4pt, text=black, font=\bfseries] {$x_{CT}$} -- (B) -- (0,-0.2) node[left, text=black, font=\bfseries] {$y_{CT}$};
  \fill[red!90!black] (B) circle (3pt) node[below=6pt, text=red!90!black, font=\bfseries\Large] {Điểm Cực Tiểu};
  \draw[thick, red!80!black, <->] (0.2, -0.2) -- (1.8, -0.2);
  \node[below, font=\footnotesize, text=gray!80!black] at (1, -0.4) {Tiếp tuyến ngang: $y'=0$};
\end{tikzpicture}
''')

# 4. Định lý đổi dấu đạo hàm (Quy tắc tìm cực trị)
tikz_04 = make_tikz_doc(r'''
\begin{tikzpicture}[font=\large]
  % Khung Cực đại
  \begin{scope}[shift={(-4.5,0)}]
    \node[font=\bfseries\Large, text=blue!90!black] at (2.2, 2.8) {1. ĐỔI DẤU $(+) \to (-)$: CỰC ĐẠI};
    \tkzTabInit[lgt=1.8,espcl=2.2,deltacl=0.6]
    {$x$ /0.9, $f'(x)$ /0.9, $f(x)$ /1.8}
    {$x_0 - h$, $x_0$, $x_0 + h$}
    \tkzTabLine{,+,0,-,}
    \tkzTabVar{-/ , +/ $f(x_0)$ (Cực đại), -/ }
  \end{scope}

  % Khung Cực tiểu
  \begin{scope}[shift={(4.5,0)}]
    \node[font=\bfseries\Large, text=red!90!black] at (2.2, 2.8) {2. ĐỔI DẤU $(-) \to (+)$: CỰC TIỂU};
    \tkzTabInit[lgt=1.8,espcl=2.2,deltacl=0.6]
    {$x$ /0.9, $f'(x)$ /0.9, $f(x)$ /1.8}
    {$x_0 - h$, $x_0$, $x_0 + h$}
    \tkzTabLine{,-,0,+,}
    \tkzTabVar{+/ , -/ $f(x_0)$ (Cực tiểu), +/ }
  \end{scope}
\end{tikzpicture}
''')

# 5. BBT Lời giải chi tiết hàm số y = x^3 - 3x^2 + 2
tikz_05 = make_tikz_doc(r'''
\begin{tikzpicture}[font=\large]
  \tkzTabInit[lgt=2.2,espcl=3.2,deltacl=0.8]
  {$x$ /1.0, $y'$ /1.0, $y$ /2.2}
  {$-\infty$, $0$, $2$, $+\infty$}
  \tkzTabLine{,+,0,-,0,+,}
  \tkzTabVar{-/ $-\infty$, +/ $2$, -/ $-2$, +/ $+\infty$}
\end{tikzpicture}
''')

# 6. Đồ thị vận dụng thực tế (Bài toán chuyển động)
tikz_06 = make_tikz_doc(r'''
\begin{tikzpicture}[>=stealth,line join=round,line cap=round,scale=1.0,font=\large]
  \draw[->, thick] (-0.8,0) -- (5.5,0) node[below] {$t\text{ (giây)}$};
  \draw[->, thick] (0,-0.8) -- (0,4.5) node[left] {$v(t)\text{ (m/s)}$};
  \node[below left] at (0,0) {$O$};

  % Do thi parabol v(t) = -t^2 + 6t
  \draw[very thick, teal!80!black, smooth, domain=0:5.2] plot (\x, {-0.3*(\x)^2 + 1.8*(\x) + 0.8});

  % Dinh van toc cuc dai tai t = 3
  \coordinate (M) at (3, 3.5);
  \draw[dashed, gray] (3,0) node[below, text=black, font=\bfseries] {$t = 3$} -- (M) -- (0,3.5) node[left, text=black, font=\bfseries] {$v_{\max} = 35$};
  \fill[red!90!black] (M) circle (3pt) node[above=4pt, text=red!90!black, font=\bfseries\Large] {Vận tốc đạt cực đại};
  
  \node[font=\normalsize, text=teal!90!black] at (4.2, 1.8) {$v'(t) = 0 \Leftrightarrow t = 3$};
  \node[font=\large, text=gray!80!black] at (2.5, -1.2) {Vận tốc tăng từ $0 \to 3$s và giảm từ sau $3$s};
\end{tikzpicture}
''')

items = [
    ("tikz_01_do_thi_don_dieu", tikz_01),
    ("tikz_02_bbt_don_dieu", tikz_02),
    ("tikz_03_minh_hoa_cuc_tri", tikz_03),
    ("tikz_04_dinh_ly_doi_dau_fphay", tikz_04),
    ("tikz_05_bbt_loi_giai", tikz_05),
    ("tikz_06_van_dung_chuyen_dong", tikz_06),
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

print("All TikZ diagrams for Toan 12 Bai 1 compiled successfully!")
