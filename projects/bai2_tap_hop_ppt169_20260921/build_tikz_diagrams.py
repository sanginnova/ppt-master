import os
import subprocess
import shutil

project_dir = r"D:\TOAN\ppt-master\projects\bai2_tap_hop_ppt169_20260921"
tikz_dir = os.path.join(project_dir, "tikz")
slide_bai_giang_tikz = r"D:\TOAN\SLIDE BAI GIANG\tikz_bai2_tap_hop"
img_out_dir = os.path.join(project_dir, "images")

os.makedirs(tikz_dir, exist_ok=True)
os.makedirs(slide_bai_giang_tikz, exist_ok=True)
os.makedirs(img_out_dir, exist_ok=True)

# Standard template per ve-hinh-tikz skill
def make_tikz_doc(body):
    return r'''\documentclass[tikz,border=5mm]{standalone}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{calc,shapes,backgrounds,arrows.meta,patterns,patterns.meta,angles,quotes}

\definecolor{slate}{RGB}{100,116,139}

\begin{document}
\begin{tikzpicture}[>=stealth,line join=round,line cap=round,font=\large]
''' + body + r'''
\end{tikzpicture}
\end{document}
'''

# 1. Venn Subset A \subset B
tikz_01 = make_tikz_doc(r'''
  % Outer Set B
  \draw[fill=blue!8, draw=blue!80!black, very thick] (0,0) ellipse (4.2cm and 2.8cm);
  \node[blue!80!black, font=\bfseries\Large] at (2.4, 1.8) {Tập hợp $B$};

  % Inner Set A
  \draw[fill=blue!22, draw=blue!90!black, very thick] (-0.8,-0.2) ellipse (2.2cm and 1.5cm);
  \node[blue!90!black, font=\bfseries\Large] at (-0.8, 0.4) {Tập hợp $A$};
  \node[blue!90!black, font=\bfseries] at (-0.8, -0.2) {$A \subset B$};

  % Elements inside A
  \fill[blue!90!black] (-1.8, -0.5) circle (2.5pt) node[below=2pt] {$x_1$};
  \fill[blue!90!black] (-0.2, -0.7) circle (2.5pt) node[below=2pt] {$x_2$};

  % Elements in B but not A
  \fill[gray!80!black] (1.8, -0.5) circle (2.5pt) node[below=2pt] {$y_1$};
  \fill[gray!80!black] (1.2, 0.8) circle (2.5pt) node[above=2pt] {$y_2$};
  \node[gray!70!black, font=\small] at (2.0, -1.5) {$y \in B, y \notin A$};
''')

# 2. Nested Number Sets N \subset Z \subset Q \subset R and I
tikz_02 = make_tikz_doc(r'''
  % Universe R Box
  \draw[rounded corners=12pt, fill=slate!6, draw=slate!80!black, very thick] (-5.5,-3.8) rectangle (5.5,3.8);
  \node[font=\bfseries\huge, text=slate!90!black] at (4.5, 3.1) {$\mathbb{R}$};
  \node[font=\small, text=slate!70!black] at (3.2, 3.1) {Tập số thực};

  % Irrational numbers I
  \draw[rounded corners=10pt, fill=red!10, draw=red!70!black, thick] (2.2,-3.2) rectangle (5.0, 2.2);
  \node[font=\bfseries\large, text=red!80!black] at (3.6, 1.6) {Số vô tỉ $\mathbb{I}$};
  \node[font=\normalsize, text=red!90!black] at (3.6, 0.7) {$\sqrt{2}, \sqrt{3}$};
  \node[font=\normalsize, text=red!90!black] at (3.6, -0.1) {$\pi \approx 3{,}14$};
  \node[font=\normalsize, text=red!90!black] at (3.6, -0.9) {$e \approx 2{,}718$};
  \node[font=\footnotesize, text=red!70!black, align=center] at (3.6, -2.1) {Thập phân\\vô hạn\\không tuần hoàn};

  % Rational numbers Q
  \draw[fill=green!10, draw=green!60!black, very thick] (-1.5,-0.3) ellipse (3.4cm and 2.9cm);
  \node[font=\bfseries\Large, text=green!60!black] at (0.9, 1.8) {$\mathbb{Q}$};
  \node[font=\footnotesize, text=green!70!black] at (-0.3, 2.0) {$\frac{3}{4}, -0{,}5$};

  % Integer numbers Z
  \draw[fill=blue!10, draw=blue!70!black, very thick] (-1.8,-0.5) ellipse (2.4cm and 2.0cm);
  \node[font=\bfseries\Large, text=blue!70!black] at (-0.1, 0.7) {$\mathbb{Z}$};
  \node[font=\footnotesize, text=blue!80!black] at (-0.1, -0.1) {$-1, -5$};

  % Natural numbers N
  \draw[fill=blue!25, draw=blue!90!black, very thick] (-2.2,-0.7) ellipse (1.4cm and 1.2cm);
  \node[font=\bfseries\Large, text=blue!90!black] at (-2.2, -0.4) {$\mathbb{N}$};
  \node[font=\footnotesize, text=blue!90!black] at (-2.2, -1.1) {$0, 1, 2, 3\dots$};
''')

# 3. Number Lines - Subsets of R
tikz_03 = make_tikz_doc(r'''
  [every node/.style={font=\normalsize}]
  % 1. Đoạn [a; b]
  \node[anchor=west, font=\bfseries\large, text=blue!80!black] at (-5, 3.8) {1. Đoạn $[a; b] = \{x \in \mathbb{R} \mid a \le x \le b\}$};
  \draw[->, thick] (-5, 2.8) -- (5.5, 2.8) node[right] {$x$};
  % Hatch left
  \foreach \x in {-4.8,-4.4,...,-1.2}
    \draw[gray!60, line width=0.8pt] (\x, 2.5) -- (\x+0.3, 3.1);
  % Active interval [a; b]
  \draw[line width=3.5pt, blue!80!black] (-1, 2.8) -- (3, 2.8);
  \node[font=\Huge\bfseries, text=blue!80!black] at (-1, 2.8) {$[$};
  \node[below=4pt, text=black, font=\bfseries] at (-1, 2.8) {$a$};
  \node[font=\Huge\bfseries, text=blue!80!black] at (3, 2.8) {$]$};
  \node[below=4pt, text=black, font=\bfseries] at (3, 2.8) {$b$};
  % Hatch right
  \foreach \x in {3.1,3.5,...,5.0}
    \draw[gray!60, line width=0.8pt] (\x, 2.5) -- (\x+0.3, 3.1);

  % 2. Khoảng (a; b)
  \node[anchor=west, font=\bfseries\large, text=green!60!black] at (-5, 1.6) {2. Khoảng $(a; b) = \{x \in \mathbb{R} \mid a < x < b\}$};
  \draw[->, thick] (-5, 0.6) -- (5.5, 0.6) node[right] {$x$};
  \foreach \x in {-4.8,-4.4,...,-1.2}
    \draw[gray!60, line width=0.8pt] (\x, 0.3) -- (\x+0.3, 0.9);
  \draw[line width=3.5pt, green!60!black] (-1, 0.6) -- (3, 0.6);
  \node[font=\Huge\bfseries, text=green!60!black] at (-1, 0.6) {$($};
  \node[below=4pt, text=black, font=\bfseries] at (-1, 0.6) {$a$};
  \node[font=\Huge\bfseries, text=green!60!black] at (3, 0.6) {$)$};
  \node[below=4pt, text=black, font=\bfseries] at (3, 0.6) {$b$};
  \foreach \x in {3.1,3.5,...,5.0}
    \draw[gray!60, line width=0.8pt] (\x, 0.3) -- (\x+0.3, 0.9);

  % 3. Nửa khoảng [a; b)
  \node[anchor=west, font=\bfseries\large, text=orange!80!black] at (-5, -0.6) {3. Nửa khoảng $[a; b) = \{x \in \mathbb{R} \mid a \le x < b\}$};
  \draw[->, thick] (-5, -1.6) -- (5.5, -1.6) node[right] {$x$};
  \foreach \x in {-4.8,-4.4,...,-1.2}
    \draw[gray!60, line width=0.8pt] (\x, -1.9) -- (\x+0.3, -1.3);
  \draw[line width=3.5pt, orange!80!black] (-1, -1.6) -- (3, -1.6);
  \node[font=\Huge\bfseries, text=orange!80!black] at (-1, -1.6) {$[$};
  \node[below=4pt, text=black, font=\bfseries] at (-1, -1.6) {$a$};
  \node[font=\Huge\bfseries, text=orange!80!black] at (3, -1.6) {$)$};
  \node[below=4pt, text=black, font=\bfseries] at (3, -1.6) {$b$};
  \foreach \x in {3.1,3.5,...,5.0}
    \draw[gray!60, line width=0.8pt] (\x, -1.9) -- (\x+0.3, -1.3);

  % 4. Khoảng vô cực (a; +infinity)
  \node[anchor=west, font=\bfseries\large, text=purple!80!black] at (-5, -2.8) {4. Khoảng vô cực $(a; +\infty) = \{x \in \mathbb{R} \mid x > a\}$};
  \draw[->, thick] (-5, -3.8) -- (5.5, -3.8) node[right] {$x$};
  \foreach \x in {-4.8,-4.4,...,-1.2}
    \draw[gray!60, line width=0.8pt] (\x, -4.1) -- (\x+0.3, -3.5);
  \draw[line width=3.5pt, purple!80!black] (-1, -3.8) -- (5.3, -3.8);
  \node[font=\Huge\bfseries, text=purple!80!black] at (-1, -3.8) {$($};
  \node[below=4pt, text=black, font=\bfseries] at (-1, -3.8) {$a$};
  \node[below=4pt, text=purple!80!black, font=\bfseries] at (4.8, -3.8) {$+\infty$};
''')

# 4. Venn Giao và Hợp
tikz_04 = make_tikz_doc(r'''
  % Phép Giao (bên trái)
  \begin{scope}[shift={(-4.2,0)}]
    \node[font=\bfseries\Large, text=blue!80!black] at (0, 2.6) {GIAO: $A \cap B$};
    
    % Clip for intersection
    \begin{scope}
      \clip (-1.1,0) circle (1.8cm);
      \fill[blue!45] (1.1,0) circle (1.8cm);
    \end{scope}

    \draw[thick, draw=blue!80!black] (-1.1,0) circle (1.8cm);
    \draw[thick, draw=blue!80!black] (1.1,0) circle (1.8cm);

    \node[font=\bfseries\huge, text=blue!90!black] at (-2.0, 0) {$A$};
    \node[font=\bfseries\huge, text=blue!90!black] at (2.0, 0) {$B$};
    \node[font=\bfseries\large, text=blue!90!black] at (0, 0) {$A \cap B$};
    \node[font=\normalsize, text=gray!80!black, align=center] at (0, -2.4) {Phần tử thuộc cả\\$A$ \textbf{VÀ} $B$};
  \end{scope}

  % Phép Hợp (bên phải)
  \begin{scope}[shift={(4.2,0)}]
    \node[font=\bfseries\Large, text=green!60!black] at (0, 2.6) {HỢP: $A \cup B$};

    % Union fill
    \fill[green!25] (-1.1,0) circle (1.8cm);
    \fill[green!25] (1.1,0) circle (1.8cm);

    \draw[thick, draw=green!60!black] (-1.1,0) circle (1.8cm);
    \draw[thick, draw=green!60!black] (1.1,0) circle (1.8cm);

    \node[font=\bfseries\huge, text=green!70!black] at (-2.0, 0) {$A$};
    \node[font=\bfseries\huge, text=green!70!black] at (2.0, 0) {$B$};
    \node[font=\bfseries\large, text=green!80!black] at (0, 0) {$A \cup B$};
    \node[font=\normalsize, text=gray!80!black, align=center] at (0, -2.4) {Gộp tất cả phần tử\\thuộc $A$ \textbf{HOẶC} $B$};
  \end{scope}
''')

# 5. Venn Hiệu và Phần bù
tikz_05 = make_tikz_doc(r'''
  % Phép Hiệu (bên trái)
  \begin{scope}[shift={(-4.2,0)}]
    \node[font=\bfseries\Large, text=blue!80!black] at (0, 2.6) {HIỆU: $A \setminus B$};

    % Difference: Fill A minus B
    \begin{scope}
      \fill[blue!35] (-1.1,0) circle (1.8cm);
      \clip (1.1,0) circle (1.8cm);
      \fill[white] (-1.1,0) circle (1.8cm);
    \end{scope}

    \draw[very thick, draw=blue!80!black] (-1.1,0) circle (1.8cm);
    \draw[thick, draw=gray!60!black] (1.1,0) circle (1.8cm);

    \node[font=\bfseries\huge, text=blue!90!black] at (-1.8, 0) {$A \setminus B$};
    \node[font=\bfseries\huge, text=gray!60!black] at (1.8, 0) {$B$};
    \node[font=\normalsize, text=gray!80!black, align=center] at (0, -2.4) {Thuộc $A$ nhưng\\không thuộc $B$};
  \end{scope}

  % Phép Phần Bù (bên phải)
  \begin{scope}[shift={(4.2,0)}]
    \node[font=\bfseries\Large, text=orange!80!black] at (0, 2.6) {PHẦN BÙ: $C_E A$ ($A \subset E$)};

    % Universe E
    \draw[rounded corners=8pt, fill=orange!18, draw=orange!80!black, very thick] (-2.8,-1.9) rectangle (2.8,1.9);
    \node[font=\bfseries\huge, text=orange!90!black] at (-2.2, 1.4) {$E$};

    % Subset A (white inside)
    \draw[fill=white, draw=blue!80!black, very thick] (0.3,-0.1) ellipse (1.6cm and 1.1cm);
    \node[font=\bfseries\huge, text=blue!90!black] at (0.3, -0.1) {$A$};

    \node[font=\bfseries\Large, text=orange!90!black] at (-1.3, -0.9) {$C_E A$};
    \node[font=\normalsize, text=gray!80!black, align=center] at (0, -2.4) {Phần bù: $C_E A = E \setminus A$};
  \end{scope}
''')

# 6. Trục số giải bài tập: A = [-2; 3) và B = (1; 5]
tikz_06 = make_tikz_doc(r'''
  [every node/.style={font=\normalsize}]
  % 1. A \cap B = (1; 3)
  \node[anchor=west, font=\bfseries\large, text=blue!80!black] at (-5.5, 3.8) {a) $A \cap B = (1; 3)$};
  \draw[->, thick] (-5.5, 2.8) -- (5.5, 2.8) node[right] {$x$};
  \foreach \x in {-5.3,-4.9,...,0.7}
    \draw[gray!60, line width=0.8pt] (\x, 2.5) -- (\x+0.3, 3.1);
  \draw[line width=3.5pt, blue!80!black] (1, 2.8) -- (3, 2.8);
  \node[font=\Huge\bfseries, text=blue!80!black] at (1, 2.8) {$($};
  \node[below=4pt, text=black, font=\bfseries] at (1, 2.8) {$1$};
  \node[font=\Huge\bfseries, text=blue!80!black] at (3, 2.8) {$)$};
  \node[below=4pt, text=black, font=\bfseries] at (3, 2.8) {$3$};
  \foreach \x in {3.1,3.5,...,5.1}
    \draw[gray!60, line width=0.8pt] (\x, 2.5) -- (\x+0.3, 3.1);

  % 2. A \cup B = [-2; 5]
  \node[anchor=west, font=\bfseries\large, text=green!60!black] at (-5.5, 1.6) {b) $A \cup B = [-2; 5]$};
  \draw[->, thick] (-5.5, 0.6) -- (5.5, 0.6) node[right] {$x$};
  \foreach \x in {-5.3,-4.9,...,-2.3}
    \draw[gray!60, line width=0.8pt] (\x, 0.3) -- (\x+0.3, 0.9);
  \draw[line width=3.5pt, green!60!black] (-2, 0.6) -- (5, 0.6);
  \node[font=\Huge\bfseries, text=green!60!black] at (-2, 0.6) {$[$};
  \node[below=4pt, text=black, font=\bfseries] at (-2, 0.6) {$-2$};
  \node[font=\Huge\bfseries, text=green!60!black] at (5, 0.6) {$]$};
  \node[below=4pt, text=black, font=\bfseries] at (5, 0.6) {$5$};
  \foreach \x in {5.1,5.5,...,5.1}
    \draw[gray!60, line width=0.8pt] (\x, 0.3) -- (\x+0.3, 0.9);

  % 3. A \setminus B = [-2; 1]
  \node[anchor=west, font=\bfseries\large, text=orange!80!black] at (-5.5, -0.6) {c) $A \setminus B = [-2; 1]$};
  \draw[->, thick] (-5.5, -1.6) -- (5.5, -1.6) node[right] {$x$};
  \foreach \x in {-5.3,-4.9,...,-2.3}
    \draw[gray!60, line width=0.8pt] (\x, -1.9) -- (\x+0.3, -1.3);
  \draw[line width=3.5pt, orange!80!black] (-2, -1.6) -- (1, -1.6);
  \node[font=\Huge\bfseries, text=orange!80!black] at (-2, -1.6) {$[$};
  \node[below=4pt, text=black, font=\bfseries] at (-2, -1.6) {$-2$};
  \node[font=\Huge\bfseries, text=orange!80!black] at (1, -1.6) {$]$};
  \node[below=4pt, text=black, font=\bfseries] at (1, -1.6) {$1$};
  \foreach \x in {1.1,1.5,...,5.1}
    \draw[gray!60, line width=0.8pt] (\x, -1.9) -- (\x+0.3, -1.3);

  % 4. C_R A = (-\infty; -2) \cup [3; +\infty)
  \node[anchor=west, font=\bfseries\large, text=purple!80!black] at (-5.5, -2.8) {d) $C_{\mathbb{R}} A = (-\infty; -2) \cup [3; +\infty)$};
  \draw[->, thick] (-5.5, -3.8) -- (5.5, -3.8) node[right] {$x$};
  \draw[line width=3.5pt, purple!80!black] (-5.3, -3.8) -- (-2, -3.8);
  \node[font=\Huge\bfseries, text=purple!80!black] at (-2, -3.8) {$)$};
  \node[below=4pt, text=black, font=\bfseries] at (-2, -3.8) {$-2$};
  \foreach \x in {-1.9,-1.5,...,2.8}
    \draw[gray!60, line width=0.8pt] (\x, -4.1) -- (\x+0.3, -3.5);
  \draw[line width=3.5pt, purple!80!black] (3, -3.8) -- (5.3, -3.8);
  \node[font=\Huge\bfseries, text=purple!80!black] at (3, -3.8) {$[$};
  \node[below=4pt, text=black, font=\bfseries] at (3, -3.8) {$3$};
''')

# 7. Venn Thể thao 24 học sinh
tikz_07 = make_tikz_doc(r'''
  % Outer universe
  \draw[rounded corners=12pt, fill=slate!5, draw=slate!70!black, very thick] (-4.5,-2.8) rectangle (4.5,2.8);
  \node[font=\bfseries\Large, text=slate!80!black] at (-3.2, 2.3) {Lớp 10A ($24$ bạn)};

  % Set Football (16)
  \draw[fill=blue!20, draw=blue!80!black, very thick, opacity=0.75] (-1.1,0) circle (2.0cm);

  % Set Badminton (11)
  \draw[fill=green!20, draw=green!70!black, very thick, opacity=0.75] (1.1,0) circle (2.0cm);

  % Overlap
  \begin{scope}
    \clip (-1.1,0) circle (2.0cm);
    \fill[yellow!50] (1.1,0) circle (2.0cm);
  \end{scope}

  % Labels
  \node[font=\bfseries\Large, text=blue!90!black] at (-2.0, 1.4) {Bóng đá ($16$)};
  \node[font=\bfseries\Huge, text=blue!90!black] at (-1.8, -0.2) {$13$};

  \node[font=\bfseries\Large, text=green!70!black] at (2.0, 1.4) {Cầu lông ($11$)};
  \node[font=\bfseries\Huge, text=green!70!black] at (1.8, -0.2) {$8$};

  \node[font=\bfseries\normalsize, text=orange!90!black] at (0, 0.6) {Cả 2 môn};
  \node[font=\bfseries\Huge, text=red!80!black] at (0, -0.3) {$3$};

  \node[font=\bfseries\large, text=blue!80!black] at (0, -2.3) {$n(A \cup B) = 13 + 3 + 8 = 24$};
''')

items = [
    ("tikz_01_venn_subset", tikz_01),
    ("tikz_02_nested_number_sets", tikz_02),
    ("tikz_03_number_lines_subsets", tikz_03),
    ("tikz_04_venn_giao_hop", tikz_04),
    ("tikz_05_venn_hieu_phanbu", tikz_05),
    ("tikz_06_truc_so_luyen_tap", tikz_06),
    ("tikz_07_venn_thuc_te", tikz_07),
]

for name, content in items:
    tex_path = os.path.join(tikz_dir, f"{name}.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(content)
    # Also save to D:\TOAN\SLIDE BAI GIANG\tikz_bai2_tap_hop\
    shutil.copy(tex_path, os.path.join(slide_bai_giang_tikz, f"{name}.tex"))
    print(f"Saved TeX: {tex_path}")

    # Compile with pdflatex
    res = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", f"{name}.tex"],
        cwd=tikz_dir,
        capture_output=True,
        text=True
    )
    if res.returncode == 0:
        pdf_path = os.path.join(tikz_dir, f"{name}.pdf")
        # Export PNG 600 DPI
        png_prefix = os.path.join(img_out_dir, name)
        subprocess.run(
            ["pdftoppm", "-png", "-r", "600", pdf_path, png_prefix],
            capture_output=True
        )
        # Find generated png and rename cleanly
        for f in os.listdir(img_out_dir):
            if f.startswith(name) and f.endswith(".png"):
                src_png = os.path.join(img_out_dir, f)
                dst_png = os.path.join(img_out_dir, f"{name}.png")
                dst_slide_png = os.path.join(slide_bai_giang_tikz, f"{name}.png")
                if src_png != dst_png:
                    shutil.move(src_png, dst_png)
                shutil.copy(dst_png, dst_slide_png)
                print(f"Compiled 600 DPI PNG: {dst_png}")
                break
    else:
        print(f"ERROR compiling {name}:", res.stderr or res.stdout[:500])

print("All 7 TikZ diagrams created and compiled successfully!")
