import os
import re
import sys

project_dir = r"D:\TOAN\ppt-master\projects\bai2_tap_hop_ppt169_20260921"
svg_out_dir = os.path.join(project_dir, "svg_output")
notes_dir = os.path.join(project_dir, "notes")
os.makedirs(svg_out_dir, exist_ok=True)
os.makedirs(notes_dir, exist_ok=True)

# Minimum font size is strictly >= 28pt across ALL slides
# All math formulas use Native Equation (OMML) via data-pptx-inline-formula
def make_svg(content, lang="vi-VN"):
    lang_attr = f' lang="{lang}"' if lang else ''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"{lang_attr} font-family="Arial, 'Segoe UI', sans-serif">
  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#F8FAFC"/>
  <rect x="0" y="0" width="1280" height="10" fill="#2563EB"/>
{content}
</svg>'''

def make_header(title, tag="BÀI 2"):
    return f'''  <!-- Header Banner (Cỡ chữ >= 28) -->
  <g id="header-group">
    <rect x="50" y="25" width="1180" height="75" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="50" y="25" width="8" height="75" rx="4" fill="#2563EB"/>
    
    <!-- Tag badge -->
    <rect x="75" y="38" width="115" height="48" rx="10" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="132" y="72" fill="#1D4ED8" font-size="28" font-weight="800" text-anchor="middle">{tag}</text>
    
    <!-- Title -->
    <text x="210" y="73" fill="#0F172A" font-size="32" font-weight="800">{title}</text>
  </g>'''

# -------------------------------------------------------------
# SLIDE 01: Cover Slide
# -------------------------------------------------------------
s01 = make_svg('''
  <circle cx="1180" cy="110" r="200" fill="#EFF6FF" opacity="0.6"/>
  <circle cx="1120" cy="620" r="160" fill="#F0FDFA" opacity="0.6"/>

  <g id="cover-card">
    <rect x="60" y="45" width="1160" height="630" rx="24" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="60" y="45" width="1160" height="14" rx="7" fill="#1E3A8A"/>

    <text x="110" y="110" fill="#1E40AF" font-size="28" font-weight="800">TRƯỜNG CĐ NGHỀ SỐ 1 - BQP • KHOA CƠ BẢN</text>
    <line x1="110" y1="130" x2="800" y2="130" stroke="#E2E8F0" stroke-width="2"/>

    <rect x="110" y="155" width="190" height="46" rx="10" fill="#DBEAFE"/>
    <text x="205" y="188" fill="#1E40AF" font-size="28" font-weight="800" text-anchor="middle">CHƯƠNG I</text>

    <text x="110" y="260" fill="#0F172A" font-size="44" font-weight="800">BÀI 2. TẬP HỢP VÀ CÁC PHÉP TOÁN</text>
    <text x="110" y="320" fill="#2563EB" font-size="44" font-weight="800">TRÊN TẬP HỢP</text>
    <text x="110" y="380" fill="#475569" font-size="28" font-weight="600">Toán 10 — Kết nối tri thức với cuộc sống</text>

    <rect x="110" y="425" width="460" height="60" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="340" y="465" fill="#0F172A" font-size="28" font-weight="700" text-anchor="middle">1. Khái niệm &amp; Các tập hợp số</text>

    <rect x="600" y="425" width="520" height="60" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="860" y="465" fill="#0F172A" font-size="28" font-weight="700" text-anchor="middle">2. Phép toán Giao, Hợp, Hiệu</text>

    <rect x="110" y="520" width="1010" height="110" rx="16" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="150" y="565" fill="#1E3A8A" font-size="30" font-weight="800">Giảng viên: ThS. Nguyễn Văn Sang</text>
    <text x="150" y="605" fill="#475569" font-size="28" font-weight="600">Khoa Cơ bản — Tiết PPCT: 03 - 04</text>
  </g>
''', lang="vi-VN")

# -------------------------------------------------------------
# SLIDE 02: Mục tiêu bài học (Native Equation)
# -------------------------------------------------------------
s02 = make_svg(make_header("MỤC TIÊU BÀI HỌC CẦN ĐẠT") + r'''
  <g id="body-grid">
    <rect x="50" y="125" width="1180" height="160" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="50" y="125" width="12" height="160" rx="6" fill="#2563EB"/>
    <text x="90" y="175" fill="#1D4ED8" font-size="30" font-weight="800">1. KIẾN THỨC TRỌNG TÂM</text>
    <text x="90" y="220" fill="#0F172A" font-size="28" font-weight="600">• Khái niệm tập hợp, tập con (<tspan data-pptx-inline-formula="A \subset B">A ⊂ B</tspan>), hai tập bằng nhau (<tspan data-pptx-inline-formula="A = B">A = B</tspan>).</text>
    <text x="90" y="262" fill="#0F172A" font-size="28" font-weight="600">• Các tập hợp số: <tspan data-pptx-inline-formula="\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}">ℕ, ℤ, ℚ, ℝ</tspan> và các tập con khoảng, đoạn của <tspan data-pptx-inline-formula="\mathbb{R}">ℝ</tspan>.</text>

    <rect x="50" y="310" width="1180" height="160" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="50" y="310" width="12" height="160" rx="6" fill="#059669"/>
    <text x="90" y="360" fill="#047857" font-size="30" font-weight="800">2. KỸ NĂNG CẦN ĐẠT</text>
    <text x="90" y="405" fill="#0F172A" font-size="28" font-weight="600">• Thực hiện thành thạo: Giao (<tspan data-pptx-inline-formula="A \cap B">A ∩ B</tspan>), Hợp (<tspan data-pptx-inline-formula="A \cup B">A ∪ B</tspan>), Hiệu (<tspan data-pptx-inline-formula="A \setminus B">A \ B</tspan>), Phần bù (<tspan data-pptx-inline-formula="C_E A">C_E A</tspan>).</text>
    <text x="90" y="447" fill="#0F172A" font-size="28" font-weight="600">• Biểu diễn chính xác các tập hợp con của <tspan data-pptx-inline-formula="\mathbb{R}">ℝ</tspan> trên trục số thực.</text>

    <rect x="50" y="495" width="1180" height="175" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="50" y="495" width="12" height="175" rx="6" fill="#D97706"/>
    <text x="90" y="545" fill="#B45309" font-size="30" font-weight="800">3. PHẨM CHẤT &amp; NĂNG LỰC SỐ</text>
    <text x="90" y="590" fill="#0F172A" font-size="28" font-weight="600">• Tư duy logic, chính xác trong việc xử lý các điều kiện mút của khoảng, đoạn.</text>
    <text x="90" y="632" fill="#0F172A" font-size="28" font-weight="600">• Ứng dụng giải quyết bài toán đếm thực tế bằng biểu đồ Ven.</text>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 03: 1. Khái niệm tập hợp (Native Equation)
# -------------------------------------------------------------
s03 = make_svg(make_header("1. KHÁI NIỆM TẬP HỢP VÀ PHẦN TỬ") + r'''
  <g id="content">
    <rect x="50" y="125" width="1180" height="150" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">A. KHÁI NIỆM CƠ BẢN</text>
    <text x="85" y="220" fill="#0F172A" font-size="28" font-weight="600">• Tập hợp là một khái niệm nguyên thủy của toán học.</text>
    <text x="85" y="258" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="a \in A">a ∈ A</tspan>: phần tử a thuộc tập A  |  <tspan data-pptx-inline-formula="b \notin A">b ∉ A</tspan>: phần tử b không thuộc A.</text>

    <rect x="50" y="300" width="1180" height="85" rx="14" fill="#FEF3C7" stroke="#FDE68A" stroke-width="2"/>
    <text x="85" y="352" fill="#92400E" font-size="28" font-weight="800">TẬP RỖNG: Ký hiệu là <tspan data-pptx-inline-formula="\emptyset">\emptyset</tspan>, là tập hợp không chứa bất kì phần tử nào.</text>

    <rect x="50" y="410" width="1180" height="260" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="455" fill="#1D4ED8" font-size="30" font-weight="800">B. HAI CÁCH XÁC ĐỊNH TẬP HỢP</text>

    <rect x="85" y="475" width="530" height="175" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="110" y="520" fill="#1E40AF" font-size="28" font-weight="800">CÁCH 1: LIỆT KÊ PHẦN TỬ</text>
    <text x="110" y="565" fill="#0F172A" font-size="28" font-weight="600">Viết trong dấu <tspan data-pptx-inline-formula="\{\dots\}">{...}</tspan>, cách nhau bởi dấu <tspan data-pptx-inline-formula=";">;</tspan></text>
    <text x="110" y="610" fill="#2563EB" font-size="28" font-weight="700">VD: <tspan data-pptx-inline-formula="P = \{2; 3; 5; 7\}">P = {2; 3; 5; 7}</tspan></text>

    <rect x="645" y="475" width="555" height="175" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="670" y="520" fill="#047857" font-size="28" font-weight="800">CÁCH 2: NÊU TÍNH CHẤT ĐẶC TRƯNG</text>
    <text x="670" y="565" fill="#0F172A" font-size="28" font-weight="600">Dạng: <tspan data-pptx-inline-formula="A = \{x \in X \mid P(x)\}">A = {x ∈ X | P(x)}</tspan></text>
    <text x="670" y="610" fill="#059669" font-size="28" font-weight="700">VD: <tspan data-pptx-inline-formula="A = \{x \in \mathbb{R} \mid x^2 - 4 = 0\}">A = {x ∈ ℝ | x² - 4 = 0}</tspan></text>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 04: 2. Tập hợp con & Biểu đồ Ven (TikZ Diagram 01)
# -------------------------------------------------------------
s04 = make_svg(make_header("2. TẬP HỢP CON VÀ BIỂU ĐỒ VEN") + r'''
  <g id="content">
    <rect x="50" y="125" width="670" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">ĐỊNH NGHĨA TẬP HỢP CON</text>
    
    <text x="85" y="230" fill="#0F172A" font-size="28" font-weight="700">Nếu mọi phần tử của A đều thuộc B:</text>
    <text x="85" y="280" fill="#1E40AF" font-size="32" font-weight="800">Ta viết: <tspan data-pptx-inline-formula="A \subset B">A ⊂ B</tspan>  (A là con của B)</text>
    <text x="85" y="325" fill="#475569" font-size="28">Logic: <tspan data-pptx-inline-formula="A \subset B \Leftrightarrow (\forall x, x \in A \Rightarrow x \in B)">A ⊂ B ⇔ (∀x, x ∈ A ⇒ x ∈ B)</tspan></text>

    <line x1="85" y1="355" x2="680" y2="355" stroke="#E2E8F0" stroke-width="2"/>
    
    <text x="85" y="405" fill="#B45309" font-size="30" font-weight="800">TÍNH CHẤT &amp; TẬP BẰNG NHAU</text>
    <text x="85" y="455" fill="#0F172A" font-size="28" font-weight="600">• Quy ước: <tspan data-pptx-inline-formula="\emptyset \subset A">∅ ⊂ A</tspan> và <tspan data-pptx-inline-formula="A \subset A">A ⊂ A</tspan> (với mọi A).</text>
    <text x="85" y="505" fill="#0F172A" font-size="28" font-weight="600">• Bắc cầu: <tspan data-pptx-inline-formula="A \subset B \land B \subset C \Rightarrow A \subset C">A ⊂ B và B ⊂ C ⇒ A ⊂ C</tspan></text>
    <text x="85" y="565" fill="#047857" font-size="28" font-weight="800">• Hai tập bằng nhau:</text>
    <text x="85" y="615" fill="#047857" font-size="30" font-weight="800">  <tspan data-pptx-inline-formula="A = B \Leftrightarrow (A \subset B \land B \subset A)">A = B ⇔ (A ⊂ B và B ⊂ A)</tspan></text>

    <!-- TikZ Diagram 01: Venn Subset -->
    <rect x="750" y="125" width="480" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="990" y="175" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN MINH HỌA</text>

    <image href="../images/tikz_01_venn_subset.png" x="770" y="195" width="440" height="315" preserveAspectRatio="xMidYMid meet"/>

    <rect x="775" y="535" width="430" height="110" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="990" y="575" fill="#1E40AF" font-size="28" font-weight="800" text-anchor="middle">A nằm trọn vẹn trong B</text>
    <text x="990" y="620" fill="#0F172A" font-size="28" font-weight="600" text-anchor="middle"><tspan data-pptx-inline-formula="\forall x_1, x_2 \in A \Rightarrow x_1, x_2 \in B">∀x ∈ A ⇒ x ∈ B</tspan></text>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 05: 3. Các tập hợp số (TikZ Diagram 02)
# -------------------------------------------------------------
s05 = make_svg(make_header("3. CÁC TẬP HỢP SỐ VÀ CHUỖI BAO HÀM") + r'''
  <g id="content">
    <rect x="50" y="120" width="1180" height="70" rx="14" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
    <text x="640" y="167" fill="#1D4ED8" font-size="34" font-weight="800" text-anchor="middle"><tspan data-pptx-inline-formula="\mathbb{N}^* \subset \mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}">ℕ* ⊂ ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ</tspan></text>

    <!-- Cột trái: Định nghĩa các tập số -->
    <rect x="50" y="205" width="600" height="465" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <g transform="translate(80, 230)">
      <text x="0" y="35" fill="#1E40AF" font-size="28" font-weight="800">1. Số tự nhiên <tspan data-pptx-inline-formula="\mathbb{N}">ℕ</tspan>:</text>
      <text x="0" y="75" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="\mathbb{N} = \{0; 1; 2; \dots\}">ℕ = {0; 1; 2; ...}</tspan> | <tspan data-pptx-inline-formula="\mathbb{N}^* = \{1; 2; \dots\}">ℕ* = {1; 2; ...}</tspan></text>

      <line x1="0" y1="105" x2="540" y2="105" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="145" fill="#1E40AF" font-size="28" font-weight="800">2. Số nguyên <tspan data-pptx-inline-formula="\mathbb{Z}">ℤ</tspan>:</text>
      <text x="0" y="185" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="\mathbb{Z} = \{\dots; -2; -1; 0; 1; 2; \dots\}">ℤ = {...; -2; -1; 0; 1; 2; ...}</tspan></text>

      <line x1="0" y1="215" x2="540" y2="215" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="255" fill="#1E40AF" font-size="28" font-weight="800">3. Số hữu tỉ <tspan data-pptx-inline-formula="\mathbb{Q}">ℚ</tspan>:</text>
      <text x="0" y="295" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="\mathbb{Q} = \{\frac{a}{b} \mid a, b \in \mathbb{Z}, b \neq 0\}">ℚ = {a/b | a,b ∈ ℤ, b ≠ 0}</tspan></text>

      <line x1="0" y1="325" x2="540" y2="325" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="365" fill="#047857" font-size="28" font-weight="800">4. Số thực <tspan data-pptx-inline-formula="\mathbb{R}">ℝ</tspan>:</text>
      <text x="0" y="405" fill="#047857" font-size="28" font-weight="700"><tspan data-pptx-inline-formula="\mathbb{R}">ℝ</tspan> gồm số hữu tỉ <tspan data-pptx-inline-formula="\mathbb{Q}">ℚ</tspan> và số vô tỉ <tspan data-pptx-inline-formula="\mathbb{I}">𝕀</tspan></text>
    </g>

    <!-- Cột phải: TikZ Diagram 02 Sơ đồ bao hàm -->
    <rect x="670" y="205" width="560" height="465" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="950" y="245" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">SƠ ĐỒ CÁC TẬP HỢP SỐ</text>
    <image href="../images/tikz_02_nested_number_sets.png" x="685" y="260" width="530" height="385" preserveAspectRatio="xMidYMid meet"/>
    <text x="950" y="660" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle"><tspan data-pptx-inline-formula="\mathbb{R} = \mathbb{Q} \cup \mathbb{I}">ℝ = ℚ ∪ 𝕀</tspan> (Vô tỉ: <tspan data-pptx-inline-formula="\sqrt{2}, \pi, e">√2, π, e</tspan>)</text>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 06: 4. Các tập con của R (TikZ Diagram 03)
# -------------------------------------------------------------
s06 = make_svg(make_header("4. CÁC TẬP CON THƯỜNG DÙNG CỦA ℝ") + r'''
  <g id="content">
    <!-- Cột trái: Tóm tắt lý thuyết -->
    <rect x="50" y="125" width="560" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    
    <g transform="translate(80, 150)">
      <text x="0" y="35" fill="#1D4ED8" font-size="30" font-weight="800">1. ĐOẠN <tspan data-pptx-inline-formula="[a; b]">[a; b]</tspan>:</text>
      <text x="0" y="75" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="[a; b] = \{x \in \mathbb{R} \mid a \le x \le b\}">[a; b] = {x ∈ ℝ | a ≤ x ≤ b}</tspan></text>
      <text x="0" y="110" fill="#2563EB" font-size="28" font-weight="700">→ Lấy cả hai đầu mút a và b</text>

      <line x1="0" y1="135" x2="500" y2="135" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="175" fill="#047857" font-size="30" font-weight="800">2. KHOẢNG <tspan data-pptx-inline-formula="(a; b)">(a; b)</tspan>:</text>
      <text x="0" y="215" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="(a; b) = \{x \in \mathbb{R} \mid a &lt; x &lt; b\}">(a; b) = {x ∈ ℝ | a &lt; x &lt; b}</tspan></text>
      <text x="0" y="250" fill="#059669" font-size="28" font-weight="700">→ Bỏ cả hai đầu mút a và b</text>

      <line x1="0" y1="275" x2="500" y2="275" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="315" fill="#D97706" font-size="30" font-weight="800">3. NỬA KHOẢNG &amp; VÔ CỰC:</text>
      <text x="0" y="355" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="[a; b) = \{x \in \mathbb{R} \mid a \le x &lt; b\}">[a; b) = {x ∈ ℝ | a ≤ x &lt; b}</tspan></text>
      <text x="0" y="395" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="(a; +\infty) = \{x \in \mathbb{R} \mid x &gt; a\}">(a; +∞) = {x ∈ ℝ | x &gt; a}</tspan></text>

      <line x1="0" y1="420" x2="500" y2="420" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="460" fill="#7C3AED" font-size="28" font-weight="800">📌 QUY TẮC: Lấy mút [ ], Bỏ ( )</text>
    </g>

    <!-- Cột phải: TikZ Diagram 03 Trục số chuẩn -->
    <rect x="630" y="125" width="600" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="930" y="170" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">HÌNH VẼ TRỤC SỐ TOÁN HỌC</text>
    <image href="../images/tikz_03_number_lines_subsets.png" x="650" y="190" width="560" height="455" preserveAspectRatio="xMidYMid meet"/>
    <text x="930" y="660" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Gạch chéo phần không thuộc tập hợp</text>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 07: 5. Phép toán Giao & Hợp (TikZ Diagram 04)
# -------------------------------------------------------------
s07 = make_svg(make_header("5. PHÉP TOÁN TẬP HỢP: GIAO VÀ HỢP") + r'''
  <g id="content">
    <!-- Hàng trên: 2 card lý thuyết song song -->
    <rect x="50" y="120" width="570" height="190" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="165" fill="#1D4ED8" font-size="30" font-weight="800">A. PHÉP GIAO (<tspan data-pptx-inline-formula="A \cap B">A ∩ B</tspan>)</text>
    <text x="85" y="210" fill="#0F172A" font-size="28" font-weight="700">Lấy các phần tử CHUNG của hai tập:</text>
    <text x="85" y="255" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="A \cap B = \{x \mid x \in A \land x \in B\}">A ∩ B = {x | x ∈ A VÀ x ∈ B}</tspan></text>
    <text x="85" y="295" fill="#166534" font-size="28" font-weight="700">VD: {1; 2; 3} ∩ {2; 3; 4} = {2; 3}</text>

    <rect x="660" y="120" width="570" height="190" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="695" y="165" fill="#047857" font-size="30" font-weight="800">B. PHÉP HỢP (<tspan data-pptx-inline-formula="A \cup B">A ∪ B</tspan>)</text>
    <text x="695" y="210" fill="#0F172A" font-size="28" font-weight="700">GỘP TẤT CẢ phần tử của hai tập:</text>
    <text x="695" y="255" fill="#047857" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="A \cup B = \{x \mid x \in A \lor x \in B\}">A ∪ B = {x | x ∈ A HOẶC x ∈ B}</tspan></text>
    <text x="695" y="295" fill="#166534" font-size="28" font-weight="700">VD: {1; 2} ∪ {2; 3; 4} = {1; 2; 3; 4}</text>

    <!-- Hàng dưới: TikZ Diagram 04 Biểu đồ Ven Giao & Hợp -->
    <rect x="50" y="325" width="1180" height="345" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="640" y="365" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN MINH HỌA GIAO VÀ HỢP</text>
    <image href="../images/tikz_04_venn_giao_hop.png" x="80" y="380" width="1120" height="275" preserveAspectRatio="xMidYMid meet"/>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 08: 6. Phép toán Hiệu & Phần bù (TikZ Diagram 05)
# -------------------------------------------------------------
s08 = make_svg(make_header("6. PHÉP TOÁN TẬP HỢP: HIỆU VÀ PHẦN BÙ") + r'''
  <g id="content">
    <!-- Hàng trên: 2 card lý thuyết song song -->
    <rect x="50" y="120" width="570" height="190" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="165" fill="#1D4ED8" font-size="30" font-weight="800">A. PHÉP HIỆU (<tspan data-pptx-inline-formula="A \setminus B">A \ B</tspan>)</text>
    <text x="85" y="210" fill="#0F172A" font-size="28" font-weight="700">Thuộc A nhưng KHÔNG thuộc B:</text>
    <text x="85" y="255" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="A \setminus B = \{x \mid x \in A, x \notin B\}">A \ B = {x | x ∈ A và x ∉ B}</tspan></text>
    <text x="85" y="295" fill="#166534" font-size="28" font-weight="700">VD: {1; 2; 3} \ {2; 4} = {1; 3}</text>

    <rect x="660" y="120" width="570" height="190" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="695" y="165" fill="#B45309" font-size="30" font-weight="800">B. PHẦN BÙ (<tspan data-pptx-inline-formula="C_E A">C_E A</tspan>)</text>
    <text x="695" y="210" fill="#0F172A" font-size="28" font-weight="700">Khi A là tập con của E (<tspan data-pptx-inline-formula="A \subset E">A ⊂ E</tspan>):</text>
    <text x="695" y="255" fill="#B45309" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="C_E A = E \setminus A">C_E A = E \ A</tspan> (Bù phần còn thiếu)</text>
    <text x="695" y="295" fill="#B45309" font-size="28" font-weight="700">VD: <tspan data-pptx-inline-formula="C_{\mathbb{R}} [0; +\infty) = (-\infty; 0)">C_ℝ [0; +∞) = (-∞; 0)</tspan></text>

    <!-- Hàng dưới: TikZ Diagram 05 Biểu đồ Ven Hiệu & Phần bù -->
    <rect x="50" y="325" width="1180" height="345" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="640" y="365" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN MINH HỌA HIỆU VÀ PHẦN BÙ</text>
    <image href="../images/tikz_05_venn_hieu_phanbu.png" x="80" y="380" width="1120" height="275" preserveAspectRatio="xMidYMid meet"/>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 09: Luyện tập - SLIDE ĐỀ BÀI (Native Equation)
# -------------------------------------------------------------
s09 = make_svg(make_header("BÀI TẬP VẬN DỤNG TRÊN TRỤC SỐ", "LUYỆN TẬP") + r'''
  <g id="exercise-content">
    <rect x="50" y="125" width="1180" height="545" rx="20" fill="#FFFFFF" stroke="#3B82F6" stroke-width="3"/>
    
    <rect x="80" y="155" width="1120" height="145" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="2"/>
    <text x="110" y="205" fill="#1D4ED8" font-size="32" font-weight="800">ĐỀ BÀI: Cho hai tập hợp con của số thực <tspan data-pptx-inline-formula="\mathbb{R}">ℝ</tspan>:</text>
    <text x="110" y="260" fill="#0F172A" font-size="34" font-weight="800">  <tspan data-pptx-inline-formula="A = [-2; 3)">A = [-2; 3)</tspan>   và   <tspan data-pptx-inline-formula="B = (1; 5]">B = (1; 5]</tspan></text>

    <g transform="translate(80, 325)">
      <rect x="0" y="0" width="545" height="95" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="30" y="58" fill="#1D4ED8" font-size="32" font-weight="800">Câu a)  Tìm <tspan data-pptx-inline-formula="A \cap B = ?">A ∩ B = ?</tspan></text>

      <rect x="575" y="0" width="545" height="95" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="605" y="58" fill="#047857" font-size="32" font-weight="800">Câu b)  Tìm <tspan data-pptx-inline-formula="A \cup B = ?">A ∪ B = ?</tspan></text>

      <rect x="0" y="120" width="545" height="95" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="30" y="178" fill="#D97706" font-size="32" font-weight="800">Câu c)  Tìm <tspan data-pptx-inline-formula="A \setminus B = ?">A \ B = ?</tspan></text>

      <rect x="575" y="120" width="545" height="95" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="605" y="178" fill="#7C3AED" font-size="32" font-weight="800">Câu d)  Tìm <tspan data-pptx-inline-formula="C_{\mathbb{R}} A = ?">C_ℝ A = ?</tspan></text>
    </g>

    <rect x="80" y="570" width="1120" height="75" rx="14" fill="#FEF2F2" stroke="#FECACA" stroke-width="2"/>
    <text x="640" y="618" fill="#991B1B" font-size="30" font-weight="800" text-anchor="middle">⏱ CẢ LỚP LÀM VÀO VỞ TRONG 5 PHÚT — VẼ TRỤC SỐ!</text>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 10: Luyện tập - SLIDE LỜI GIẢI (TikZ Diagram 06)
# -------------------------------------------------------------
s10 = make_svg(make_header("HƯỚNG DẪN GIẢI BÀI TẬP VẬN DỤNG", "LỜI GIẢI") + r'''
  <g id="solution-content">
    <!-- Cột trái: Kết quả chi tiết -->
    <rect x="50" y="125" width="560" height="545" rx="20" fill="#FFFFFF" stroke="#10B981" stroke-width="3"/>
    
    <g transform="translate(75, 145)">
      <rect x="0" y="0" width="510" height="95" rx="12" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
      <text x="20" y="40" fill="#1D4ED8" font-size="28" font-weight="800">a) Phép Giao <tspan data-pptx-inline-formula="A \cap B">A ∩ B</tspan>:</text>
      <text x="20" y="78" fill="#1E40AF" font-size="30" font-weight="800">⇒ <tspan data-pptx-inline-formula="A \cap B = (1; 3)">A ∩ B = (1; 3)</tspan></text>

      <rect x="0" y="110" width="510" height="95" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
      <text x="20" y="150" fill="#047857" font-size="28" font-weight="800">b) Phép Hợp <tspan data-pptx-inline-formula="A \cup B">A ∪ B</tspan>:</text>
      <text x="20" y="188" fill="#166534" font-size="30" font-weight="800">⇒ <tspan data-pptx-inline-formula="A \cup B = [-2; 5]">A ∪ B = [-2; 5]</tspan></text>

      <rect x="0" y="220" width="510" height="95" rx="12" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
      <text x="20" y="260" fill="#D97706" font-size="28" font-weight="800">c) Phép Hiệu <tspan data-pptx-inline-formula="A \setminus B">A \ B</tspan>:</text>
      <text x="20" y="298" fill="#B45309" font-size="30" font-weight="800">⇒ <tspan data-pptx-inline-formula="A \setminus B = [-2; 1]">A \ B = [-2; 1]</tspan></text>

      <rect x="0" y="330" width="510" height="95" rx="12" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
      <text x="20" y="370" fill="#7C3AED" font-size="28" font-weight="800">d) Phần bù <tspan data-pptx-inline-formula="C_{\mathbb{R}} A">C_ℝ A</tspan>:</text>
      <text x="20" y="408" fill="#6B21A8" font-size="28" font-weight="800">⇒ <tspan data-pptx-inline-formula="(-\infty; -2) \cup [3; +\infty)">(-∞; -2) ∪ [3; +∞)</tspan></text>

      <text x="20" y="465" fill="#DC2626" font-size="28" font-weight="800">⚠️ LƯU Ý: 1 ∉ B nên 1 ∈ A \ B</text>
    </g>

    <!-- Cột phải: TikZ Diagram 06 Trục số 4 phép toán -->
    <rect x="630" y="125" width="600" height="545" rx="20" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="930" y="170" fill="#047857" font-size="30" font-weight="800" text-anchor="middle">BIỂU DIỄN 4 PHÉP TOÁN TRÊN TRỤC SỐ</text>
    <image href="../images/tikz_06_truc_so_luyen_tap.png" x="650" y="188" width="560" height="460" preserveAspectRatio="xMidYMid meet"/>
    <text x="930" y="660" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Đổi ngoặc tròn thành vuông khi lấy hiệu và bù</text>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 11: Bài toán thực tế (TikZ Diagram 07)
# -------------------------------------------------------------
s11 = make_svg(make_header("ỨNG DỤNG THỰC TẾ &amp; CÔNG THỨC ĐẾM") + r'''
  <g id="content">
    <!-- Cột trái: Lời giải bài toán -->
    <rect x="50" y="125" width="580" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">BÀI TOÁN THỂ THAO (SGK TR.18)</text>

    <text x="85" y="225" fill="#0F172A" font-size="28" font-weight="600">Lớp 10A có 24 bạn thi đấu thể thao:</text>
    <text x="85" y="270" fill="#1E40AF" font-size="28" font-weight="700">• Bóng đá: 16 bạn  |  Cầu lông: 11 bạn.</text>
    <text x="85" y="315" fill="#B91C1C" font-size="30" font-weight="800">Hỏi: Có bao nhiêu bạn thi cả 2 môn?</text>

    <line x1="85" y1="345" x2="590" y2="345" stroke="#E2E8F0" stroke-width="2"/>

    <text x="85" y="390" fill="#047857" font-size="30" font-weight="800">CÔNG THỨC SỐ PHẦN TỬ:</text>
    <rect x="85" y="415" width="510" height="80" rx="14" fill="#FEF3C7" stroke="#FDE68A" stroke-width="2"/>
    <text x="340" y="465" fill="#B45309" font-size="28" font-weight="800" text-anchor="middle"><tspan data-pptx-inline-formula="n(A \cup B) = n(A) + n(B) - n(A \cap B)">n(A ∪ B) = n(A) + n(B) - n(A ∩ B)</tspan></text>

    <text x="85" y="540" fill="#0F172A" font-size="28" font-weight="700">Suy ra: <tspan data-pptx-inline-formula="n(A \cap B) = 16 + 11 - 24 = 3">n(A ∩ B) = 16 + 11 - 24 = 3</tspan></text>
    <text x="85" y="605" fill="#047857" font-size="34" font-weight="800">⇒ Kết quả: Có 3 bạn thi cả 2 môn!</text>

    <!-- Cột phải: TikZ Diagram 07 Biểu đồ Ven thể thao -->
    <rect x="650" y="125" width="580" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="940" y="175" fill="#047857" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN PHÂN BỔ HỌC SINH</text>
    <image href="../images/tikz_07_venn_thuc_te.png" x="670" y="200" width="540" height="345" preserveAspectRatio="xMidYMid meet"/>
    <rect x="675" y="565" width="530" height="85" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="940" y="618" fill="#0F172A" font-size="28" font-weight="700" text-anchor="middle">Tổng kiểm tra: 13 + 3 + 8 = 24 bạn</text>
  </g>
''', lang="")

# -------------------------------------------------------------
# SLIDE 12: Tổng kết & Dặn dò (Native Equation)
# -------------------------------------------------------------
s12 = make_svg(make_header("TỔNG KẾT BÀI HỌC VÀ DẶN DÒ", "TỔNG KẾT") + r'''
  <g id="content">
    <rect x="50" y="125" width="670" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">4 GHI NHỚ TRỌNG TÂM</text>

    <g transform="translate(85, 200)">
      <text x="0" y="40" fill="#0F172A" font-size="28" font-weight="700">1. Tập con:</text>
      <text x="170" y="40" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="A \subset B">A ⊂ B</tspan> | <tspan data-pptx-inline-formula="A = B">A = B</tspan></text>

      <line x1="0" y1="75" x2="600" y2="75" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="125" fill="#0F172A" font-size="28" font-weight="700">2. Chuỗi số:</text>
      <text x="170" y="125" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}">ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ</tspan></text>

      <line x1="0" y1="160" x2="600" y2="160" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="210" fill="#0F172A" font-size="28" font-weight="700">3. Phép toán:</text>
      <text x="170" y="210" fill="#047857" font-size="28" font-weight="800">Giao <tspan data-pptx-inline-formula="\cap">∩</tspan>, Hợp <tspan data-pptx-inline-formula="\cup">∪</tspan>, Hiệu <tspan data-pptx-inline-formula="\setminus">\</tspan>, Phần bù</text>

      <line x1="0" y1="245" x2="600" y2="245" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="295" fill="#0F172A" font-size="28" font-weight="700">4. Trục số:</text>
      <text x="170" y="295" fill="#D97706" font-size="28" font-weight="800">Lấy [ ], bỏ ( ), gạch phần ngoài</text>
    </g>

    <rect x="750" y="125" width="480" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="785" y="175" fill="#9333EA" font-size="30" font-weight="800">NHIỆM VỤ VỀ NHÀ</text>

    <rect x="775" y="210" width="430" height="195" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="800" y="260" fill="#0F172A" font-size="28" font-weight="700">• Làm bài 1.8 đến 1.16</text>
    <text x="800" y="305" fill="#64748B" font-size="28">  (SGK Toán 10, trang 19)</text>
    <text x="800" y="360" fill="#1E40AF" font-size="28" font-weight="700">• Chuẩn bị: Bài tập cuối Ch.1</text>

    <rect x="775" y="435" width="430" height="210" rx="16" fill="#0F172A"/>
    <text x="990" y="495" fill="#FFFFFF" font-size="32" font-weight="800" text-anchor="middle">CHÚC CÁC EM</text>
    <text x="990" y="540" fill="#38BDF8" font-size="32" font-weight="800" text-anchor="middle">HỌC TỐT MÔN TOÁN!</text>
    <text x="990" y="605" fill="#94A3B8" font-size="28" font-weight="600" text-anchor="middle">Thầy Nguyễn Văn Sang</text>
  </g>
''', lang="")

slides = [
    ("01_cover.svg", s01),
    ("02_muc_tieu.svg", s02),
    ("03_khai_niem_tap_hop.svg", s03),
    ("04_tap_con_ven.svg", s04),
    ("05_cac_tap_hop_so.svg", s05),
    ("06_khoang_doan_truc_so.svg", s06),
    ("07_phep_toan_giao_hop.svg", s07),
    ("08_phep_toan_hieu_phan_bu.svg", s08),
    ("09_luyen_tap_de_bai.svg", s09),
    ("10_luyen_tap_loi_giai.svg", s10),
    ("11_bai_toan_thuc_te.svg", s11),
    ("12_tong_ket_nhiem_vu.svg", s12)
]

# Strict Font Size Check
min_font = 999
for fname, content in slides:
    matches = re.findall(r'font-size="(\d+)"', content)
    for m in matches:
        val = int(m)
        if val < min_font:
            min_font = val
        if val < 28:
            print(f"ERROR: {fname} has font-size {val} < 28!")
            sys.exit(1)

print(f"STRICT CHECK PASSED! Minimum font-size across all slides is: {min_font} (>= 28)")

for filename, content in slides:
    filepath = os.path.join(svg_out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated (font >= 28, native equation, tikz embedded): {filepath}")

print("All 12 slides generated with font-size >= 28, Native Equation OMML, and TikZ Diagrams!")
