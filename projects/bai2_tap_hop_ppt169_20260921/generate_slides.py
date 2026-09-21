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
    <rect x="75" y="38" width="120" height="48" rx="10" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="135" y="72" fill="#1D4ED8" font-size="28" font-weight="800" text-anchor="middle">{tag}</text>
    
    <!-- Title -->
    <text x="215" y="73" fill="#0F172A" font-size="30" font-weight="800">{title}</text>
  </g>'''

# =============================================================
# SLIDE 01: Cover Slide
# =============================================================
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
    <text x="110" y="380" fill="#475569" font-size="28" font-weight="600">Toán 10 — Sách Kết nối tri thức với cuộc sống</text>

    <rect x="110" y="425" width="460" height="60" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="340" y="465" fill="#0F172A" font-size="28" font-weight="700" text-anchor="middle">1. Khái niệm &amp; Các tập hợp số</text>

    <rect x="600" y="425" width="520" height="60" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="860" y="465" fill="#0F172A" font-size="28" font-weight="700" text-anchor="middle">2. Phép toán Giao, Hợp, Hiệu</text>

    <rect x="110" y="520" width="1010" height="110" rx="16" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="150" y="565" fill="#1E3A8A" font-size="30" font-weight="800">Giảng viên: ThS. Nguyễn Văn Sang</text>
    <text x="150" y="605" fill="#475569" font-size="28" font-weight="600">Khoa Cơ bản — Tiết PPCT: 03 - 04</text>
  </g>
''', lang="vi-VN")

# =============================================================
# SLIDE 02: Mục tiêu bài học (Native Equation)
# =============================================================
s02 = make_svg(make_header("MỤC TIÊU BÀI HỌC CẦN ĐẠT", "MỤC TIÊU") + r'''
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

# =============================================================
# SLIDE 03: 1.a. Tập hợp và phần tử (SGK Mục 1.a)
# =============================================================
s03 = make_svg(make_header("1. CÁC KHÁI NIỆM CƠ BẢN: a. Tập hợp và phần tử", "MỤC 1.a") + r'''
  <g id="content">
    <rect x="50" y="125" width="1180" height="150" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">A. KHÁI NIỆM CƠ BẢN VÀ KÝ HIỆU</text>
    <text x="85" y="220" fill="#0F172A" font-size="28" font-weight="600">• Tập hợp là một khái niệm nguyên thủy của toán học.</text>
    <text x="85" y="258" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="a \in A">a ∈ A</tspan>: a thuộc tập hợp A  |  <tspan data-pptx-inline-formula="b \notin A">b ∉ A</tspan>: b không thuộc tập hợp A.</text>

    <rect x="50" y="300" width="1180" height="85" rx="14" fill="#FEF3C7" stroke="#FDE68A" stroke-width="2"/>
    <text x="85" y="352" fill="#92400E" font-size="28" font-weight="800">TẬP RỖNG: Ký hiệu là <tspan data-pptx-inline-formula="\emptyset">\emptyset</tspan>, là tập hợp không chứa bất kì phần tử nào.</text>

    <rect x="50" y="410" width="1180" height="260" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="455" fill="#1D4ED8" font-size="30" font-weight="800">B. HAI CÁCH XÁC ĐỊNH TẬP HỢP (SGK KNTT)</text>

    <rect x="85" y="475" width="530" height="175" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="110" y="520" fill="#1E40AF" font-size="28" font-weight="800">CÁCH 1: LIỆT KÊ PHẦN TỬ</text>
    <text x="110" y="565" fill="#0F172A" font-size="28" font-weight="600">Viết trong dấu <tspan data-pptx-inline-formula="\{\dots\}">{...}</tspan>, cách nhau bởi dấu <tspan data-pptx-inline-formula=";">;</tspan></text>
    <text x="110" y="610" fill="#2563EB" font-size="28" font-weight="700">VD: <tspan data-pptx-inline-formula="P = \{2; 3; 5; 7\}">P = {2; 3; 5; 7}</tspan></text>

    <rect x="645" y="475" width="555" height="175" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="670" y="520" fill="#047857" font-size="28" font-weight="800">CÁCH 2: CHỈ RA TÍNH CHẤT ĐẶC TRƯNG</text>
    <text x="670" y="565" fill="#0F172A" font-size="28" font-weight="600">Dạng: <tspan data-pptx-inline-formula="A = \{x \in X \mid P(x)\}">A = {x ∈ X | P(x)}</tspan></text>
    <text x="670" y="610" fill="#059669" font-size="28" font-weight="700">VD: <tspan data-pptx-inline-formula="A = \{x \in \mathbb{R} \mid x^2 - 4 = 0\}">A = {x ∈ ℝ | x² - 4 = 0}</tspan></text>
  </g>
''', lang="")

# =============================================================
# SLIDE 04: 1.b,c. Tập hợp con & Hai tập bằng nhau (SGK Mục 1.b, 1.c)
# =============================================================
s04 = make_svg(make_header("1. CÁC KHÁI NIỆM CƠ BẢN: b. Tập con &amp; c. Hai tập bằng nhau", "MỤC 1.b,c") + r'''
  <g id="content">
    <rect x="50" y="125" width="670" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">b. ĐỊNH NGHĨA TẬP HỢP CON</text>
    
    <text x="85" y="230" fill="#0F172A" font-size="28" font-weight="700">Nếu mọi phần tử của A đều thuộc B:</text>
    <text x="85" y="280" fill="#1E40AF" font-size="32" font-weight="800">Ta viết: <tspan data-pptx-inline-formula="A \subset B">A ⊂ B</tspan>  (A là tập con của B)</text>
    <text x="85" y="325" fill="#475569" font-size="28">Logic: <tspan data-pptx-inline-formula="A \subset B \Leftrightarrow (\forall x, x \in A \Rightarrow x \in B)">A ⊂ B ⇔ (∀x, x ∈ A ⇒ x ∈ B)</tspan></text>

    <line x1="85" y1="355" x2="680" y2="355" stroke="#E2E8F0" stroke-width="2"/>
    
    <text x="85" y="405" fill="#B45309" font-size="30" font-weight="800">c. TÍNH CHẤT &amp; HAI TẬP BẰNG NHAU</text>
    <text x="85" y="455" fill="#0F172A" font-size="28" font-weight="600">• Quy ước: <tspan data-pptx-inline-formula="\emptyset \subset A">\emptyset \subset A</tspan> và <tspan data-pptx-inline-formula="A \subset A">A \subset A</tspan> (với mọi tập A).</text>
    <text x="85" y="505" fill="#0F172A" font-size="28" font-weight="600">• Tính bắc cầu: <tspan data-pptx-inline-formula="A \subset B \land B \subset C \Rightarrow A \subset C">A ⊂ B và B ⊂ C ⇒ A ⊂ C</tspan></text>
    <text x="85" y="565" fill="#047857" font-size="28" font-weight="800">• Định nghĩa hai tập bằng nhau:</text>
    <text x="85" y="615" fill="#047857" font-size="30" font-weight="800">  <tspan data-pptx-inline-formula="A = B \Leftrightarrow (A \subset B \land B \subset A)">A = B ⇔ (A ⊂ B và B ⊂ A)</tspan></text>

    <!-- TikZ 01: Biểu đồ Ven tập con -->
    <rect x="750" y="125" width="480" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="990" y="175" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN (HÌNH 1.2 SGK)</text>

    <image href="../images/tikz_01_venn_subset.png" x="770" y="195" width="440" height="315" preserveAspectRatio="xMidYMid meet"/>

    <rect x="775" y="535" width="430" height="110" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="990" y="575" fill="#1E40AF" font-size="28" font-weight="800" text-anchor="middle">Tập A nằm trọn vẹn trong B</text>
    <text x="990" y="620" fill="#0F172A" font-size="28" font-weight="600" text-anchor="middle"><tspan data-pptx-inline-formula="\forall x \in A \Rightarrow x \in B">∀x ∈ A ⇒ x ∈ B</tspan></text>
  </g>
''', lang="")

# =============================================================
# SLIDE 05: 2.a. Mối quan hệ giữa các tập hợp số (SGK Mục 2.a)
# =============================================================
s05 = make_svg(make_header("2. CÁC TẬP HỢP SỐ: a. Mối quan hệ giữa các tập hợp số", "MỤC 2.a") + r'''
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

# =============================================================
# SLIDE 06: 2.b. Các tập con của R — Khoảng và Đoạn (SGK Mục 2.b Phần 1)
# =============================================================
s06 = make_svg(make_header("2. CÁC TẬP HỢP SỐ: b. Các tập con của ℝ — Khoảng &amp; Đoạn", "MỤC 2.b") + r'''
  <g id="content">
    <!-- Cột trái: Định nghĩa Khoảng & Đoạn -->
    <rect x="50" y="125" width="560" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    
    <g transform="translate(80, 155)">
      <!-- 1. Đoạn [a; b] -->
      <rect x="0" y="0" width="500" height="195" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
      <text x="20" y="45" fill="#1D4ED8" font-size="30" font-weight="800">1. ĐOẠN <tspan data-pptx-inline-formula="[a; b]">[a; b]</tspan>:</text>
      <text x="20" y="90" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="[a; b] = \{x \in \mathbb{R} \mid a \le x \le b\}">[a; b] = {x ∈ ℝ | a ≤ x ≤ b}</tspan></text>
      <text x="20" y="130" fill="#1E40AF" font-size="28" font-weight="700">Ký hiệu mút: Dùng ngoặc vuông [ ]</text>
      <text x="20" y="170" fill="#047857" font-size="28" font-weight="800">→ LẤY CẢ HAI ĐẦU MÚT a VÀ b</text>

      <!-- 2. Khoảng (a; b) -->
      <rect x="0" y="215" width="500" height="195" rx="14" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
      <text x="20" y="260" fill="#047857" font-size="30" font-weight="800">2. KHOẢNG <tspan data-pptx-inline-formula="(a; b)">(a; b)</tspan>:</text>
      <text x="20" y="305" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="(a; b) = \{x \in \mathbb{R} \mid a &lt; x &lt; b\}">(a; b) = {x ∈ ℝ | a &lt; x &lt; b}</tspan></text>
      <text x="20" y="345" fill="#065F46" font-size="28" font-weight="700">Ký hiệu mút: Dùng ngoặc tròn ( )</text>
      <text x="20" y="385" fill="#DC2626" font-size="28" font-weight="800">→ BỎ CẢ HAI ĐẦU MÚT a VÀ b</text>

      <text x="20" y="465" fill="#475569" font-size="28" font-weight="600">a, b được gọi là các đầu mút của tập hợp</text>
    </g>

    <!-- Cột phải: TikZ Diagram 03A Trục số Khoảng và Đoạn -->
    <rect x="630" y="125" width="600" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="930" y="170" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">BIỂU DIỄN TRÊN TRỤC SỐ THỰC</text>
    <image href="../images/tikz_03a_khoang_doan.png" x="650" y="190" width="560" height="420" preserveAspectRatio="xMidYMid meet"/>
    <text x="930" y="645" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Quy ước SGK: Gạch chéo phần ngoài tập</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 07: 2.b. Các tập con của R — Nửa khoảng & Vô cực (SGK Mục 2.b Phần 2)
# =============================================================
s07 = make_svg(make_header("2. CÁC TẬP HỢP SỐ: b. Nửa khoảng &amp; Khoảng vô cực", "MỤC 2.b") + r'''
  <g id="content">
    <!-- Cột trái: Định nghĩa Nửa khoảng & Vô cực -->
    <rect x="50" y="125" width="560" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    
    <g transform="translate(80, 150)">
      <text x="0" y="35" fill="#D97706" font-size="30" font-weight="800">3. NỬA KHOẢNG (LẤY 1 MÚT):</text>
      <text x="0" y="75" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="[a; b) = \{x \in \mathbb{R} \mid a \le x &lt; b\}">[a; b) = {x ∈ ℝ | a ≤ x &lt; b}</tspan></text>
      <text x="0" y="115" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="(a; b] = \{x \in \mathbb{R} \mid a &lt; x \le b\}">(a; b] = {x ∈ ℝ | a &lt; x ≤ b}</tspan></text>

      <line x1="0" y1="140" x2="500" y2="140" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="180" fill="#7C3AED" font-size="30" font-weight="800">4. KHOẢNG VÔ CỰC:</text>
      <text x="0" y="220" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="[a; +\infty) = \{x \in \mathbb{R} \mid x \ge a\}">[a; +∞) = {x ∈ ℝ | x ≥ a}</tspan></text>
      <text x="0" y="260" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="(a; +\infty) = \{x \in \mathbb{R} \mid x &gt; a\}">(a; +∞) = {x ∈ ℝ | x &gt; a}</tspan></text>
      <text x="0" y="300" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="(-\infty; b) = \{x \in \mathbb{R} \mid x &lt; b\}">(-∞; b) = {x ∈ ℝ | x &lt; b}</tspan></text>
      <text x="0" y="340" fill="#0F172A" font-size="28" font-weight="600">• <tspan data-pptx-inline-formula="(-\infty; +\infty) = \mathbb{R}">(-∞; +∞) = ℝ</tspan></text>

      <rect x="0" y="375" width="500" height="110" rx="12" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
      <text x="15" y="415" fill="#92400E" font-size="28" font-weight="800">QUY TẮC VÀNG TRỤC SỐ:</text>
      <text x="15" y="455" fill="#0F172A" font-size="28" font-weight="600">Lấy mút: [ ]. Bỏ mút: ( ). Gạch bỏ ngoài tập.</text>
    </g>

    <!-- Cột phải: TikZ Diagram 03B Trục số Nửa khoảng & Vô cực -->
    <rect x="630" y="125" width="600" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="930" y="165" fill="#D97706" font-size="30" font-weight="800" text-anchor="middle">HÌNH VẼ TRỤC SỐ NỬA KHOẢNG</text>
    <image href="../images/tikz_03b_nua_khoang_vo_cuc.png" x="650" y="180" width="560" height="470" preserveAspectRatio="xMidYMid meet"/>
  </g>
''', lang="")

# =============================================================
# SLIDE 08: 3.a. Giao của hai tập hợp (SGK Mục 3.a)
# =============================================================
s08 = make_svg(make_header("3. CÁC PHÉP TOÁN TRÊN TẬP HỢP: a. Giao của hai tập hợp", "MỤC 3.a") + r'''
  <g id="content">
    <rect x="50" y="125" width="670" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">ĐỊNH NGHĨA PHÉP GIAO (SGK KNTT)</text>
    
    <text x="85" y="230" fill="#0F172A" font-size="28" font-weight="700">Tập hợp gồm các phần tử thuộc cả A VÀ B:</text>
    <rect x="85" y="255" width="600" height="85" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="2"/>
    <text x="385" y="308" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle"><tspan data-pptx-inline-formula="A \cap B = \{x \mid x \in A \text{ và } x \in B\}">A ∩ B = {x | x ∈ A và x ∈ B}</tspan></text>

    <text x="85" y="380" fill="#475569" font-size="28">Logic: <tspan data-pptx-inline-formula="x \in A \cap B \Leftrightarrow (x \in A \land x \in B)">x ∈ A ∩ B ⇔ (x ∈ A và x ∈ B)</tspan></text>

    <line x1="85" y1="410" x2="680" y2="410" stroke="#E2E8F0" stroke-width="2"/>

    <text x="85" y="460" fill="#047857" font-size="30" font-weight="800">VÍ DỤ 6 (SGK TRANG 16):</text>
    <text x="85" y="505" fill="#0F172A" font-size="28" font-weight="600">Cho <tspan data-pptx-inline-formula="A = \{1; 2; 3; 4\}">A = {1; 2; 3; 4}</tspan> và <tspan data-pptx-inline-formula="B = \{2; 4; 6\}">B = {2; 4; 6}</tspan>.</text>
    <rect x="85" y="530" width="600" height="85" rx="14" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
    <text x="110" y="582" fill="#166534" font-size="30" font-weight="800">⇒ Giao: <tspan data-pptx-inline-formula="A \cap B = \{2; 4\}">A ∩ B = {2; 4}</tspan> (phần tử chung)</text>

    <!-- TikZ 04: Biểu đồ Ven Giao -->
    <rect x="750" y="125" width="480" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="990" y="175" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN PHÉP GIAO</text>
    <image href="../images/tikz_04_giao.png" x="770" y="200" width="440" height="380" preserveAspectRatio="xMidYMid meet"/>
    <text x="990" y="635" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Phần giao được tô màu đậm</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 09: 3.b. Hợp của hai tập hợp (SGK Mục 3.b)
# =============================================================
s09 = make_svg(make_header("3. CÁC PHÉP TOÁN TRÊN TẬP HỢP: b. Hợp của hai tập hợp", "MỤC 3.b") + r'''
  <g id="content">
    <rect x="50" y="125" width="670" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#047857" font-size="30" font-weight="800">ĐỊNH NGHĨA PHÉP HỢP (SGK KNTT)</text>
    
    <text x="85" y="230" fill="#0F172A" font-size="28" font-weight="700">Gộp tất cả các phần tử thuộc A HOẶC thuộc B:</text>
    <rect x="85" y="255" width="600" height="85" rx="14" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="2"/>
    <text x="385" y="308" fill="#047857" font-size="30" font-weight="800" text-anchor="middle"><tspan data-pptx-inline-formula="A \cup B = \{x \mid x \in A \text{ hoặc } x \in B\}">A ∪ B = {x | x ∈ A hoặc x ∈ B}</tspan></text>

    <text x="85" y="380" fill="#475569" font-size="28">Logic: <tspan data-pptx-inline-formula="x \in A \cup B \Leftrightarrow (x \in A \lor x \in B)">x ∈ A ∪ B ⇔ (x ∈ A hoặc x ∈ B)</tspan></text>

    <line x1="85" y1="410" x2="680" y2="410" stroke="#E2E8F0" stroke-width="2"/>

    <text x="85" y="460" fill="#1D4ED8" font-size="30" font-weight="800">VÍ DỤ 7 (SGK TRANG 17):</text>
    <text x="85" y="505" fill="#0F172A" font-size="28" font-weight="600">Cho <tspan data-pptx-inline-formula="A = \{a; b; c\}">A = {a; b; c}</tspan> và <tspan data-pptx-inline-formula="B = \{c; d; e\}">B = {c; d; e}</tspan>.</text>
    <rect x="85" y="530" width="600" height="85" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="110" y="582" fill="#1E40AF" font-size="30" font-weight="800">⇒ Hợp: <tspan data-pptx-inline-formula="A \cup B = \{a; b; c; d; e\}">A ∪ B = {a; b; c; d; e}</tspan></text>

    <!-- TikZ 05: Biểu đồ Ven Hợp -->
    <rect x="750" y="125" width="480" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="990" y="175" fill="#047857" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN PHÉP HỢP</text>
    <image href="../images/tikz_05_hop.png" x="770" y="200" width="440" height="380" preserveAspectRatio="xMidYMid meet"/>
    <text x="990" y="635" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Toàn bộ 2 tập được tô màu</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 10: 3.c. Hiệu của hai tập hợp & Phần bù (SGK Mục 3.c)
# =============================================================
s10 = make_svg(make_header("3. CÁC PHÉP TOÁN: c. Hiệu của hai tập hợp &amp; Phần bù", "MỤC 3.c") + r'''
  <g id="content">
    <!-- Cột trái: Định nghĩa Hiệu & Phần bù -->
    <rect x="50" y="125" width="670" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">1. ĐỊNH NGHĨA PHÉP HIỆU (<tspan data-pptx-inline-formula="A \setminus B">A \ B</tspan>)</text>
    <text x="85" y="220" fill="#0F172A" font-size="28" font-weight="700">Gồm các phần tử thuộc A nhưng KHÔNG thuộc B:</text>
    <rect x="85" y="245" width="600" height="75" rx="12" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="385" y="292" fill="#1E40AF" font-size="28" font-weight="800" text-anchor="middle"><tspan data-pptx-inline-formula="A \setminus B = \{x \mid x \in A \text{ và } x \notin B\}">A \ B = {x | x ∈ A và x ∉ B}</tspan></text>

    <line x1="85" y1="340" x2="680" y2="340" stroke="#E2E8F0" stroke-width="2"/>

    <text x="85" y="385" fill="#B45309" font-size="30" font-weight="800">2. ĐỊNH NGHĨA PHẦN BÙ (<tspan data-pptx-inline-formula="C_E A">C_E A</tspan>)</text>
    <text x="85" y="430" fill="#0F172A" font-size="28" font-weight="700">Khi A là tập con của E (<tspan data-pptx-inline-formula="A \subset E">A ⊂ E</tspan>):</text>
    <rect x="85" y="455" width="600" height="75" rx="12" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="385" y="502" fill="#B45309" font-size="28" font-weight="800" text-anchor="middle"><tspan data-pptx-inline-formula="C_E A = E \setminus A">C_E A = E \ A</tspan> (Phần còn thiếu để đủ E)</text>

    <rect x="85" y="555" width="600" height="95" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="105" y="595" fill="#0F172A" font-size="28" font-weight="700">VD: <tspan data-pptx-inline-formula="C_{\mathbb{R}} [0; +\infty) = \mathbb{R} \setminus [0; +\infty) = (-\infty; 0)">C_ℝ [0; +∞) = ℝ \ [0; +∞) = (-∞; 0)</tspan></text>
    <text x="105" y="635" fill="#DC2626" font-size="28" font-weight="700">⚠️ Lưu ý: Đổi mút từ ngoặc vuông sang tròn!</text>

    <!-- TikZ 06: Biểu đồ Ven Hiệu và Phần bù -->
    <rect x="750" y="125" width="480" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="990" y="175" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN MINH HỌA</text>
    <image href="../images/tikz_06_hieu_phanbu.png" x="760" y="220" width="460" height="340" preserveAspectRatio="xMidYMid meet"/>
    <text x="990" y="635" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Vùng khuyết (Hiệu) &amp; Khung E (Phần bù)</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 11: Luyện tập - BÀI TẬP 1.15 SGK TRANG 19 (ĐỀ BÀI)
# =============================================================
s11 = make_svg(make_header("BÀI TẬP 1.15 SGK TRANG 19 — TRỤC SỐ THỰC", "LUYỆN TẬP") + r'''
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
    <text x="640" y="618" fill="#991B1B" font-size="30" font-weight="800" text-anchor="middle">⏱ CẢ LỚP LÀM VÀO VỞ TRONG 5 PHÚT — BIỂU DIỄN TRÊN TRỤC SỐ!</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 12: Luyện tập - HƯỚNG DẪN GIẢI BÀI 1.15 (TikZ 07)
# =============================================================
s12 = make_svg(make_header("HƯỚNG DẪN GIẢI CHI TIẾT BÀI 1.15 TRÊN TRỤC SỐ", "LỜI GIẢI") + r'''
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

    <!-- Cột phải: TikZ 07 Trục số 4 phép toán -->
    <rect x="630" y="125" width="600" height="545" rx="20" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="930" y="170" fill="#047857" font-size="30" font-weight="800" text-anchor="middle">BIỂU DIỄN 4 PHÉP TOÁN TRÊN TRỤC SỐ</text>
    <image href="../images/tikz_07_truc_so_luyen_tap.png" x="650" y="188" width="560" height="460" preserveAspectRatio="xMidYMid meet"/>
    <text x="930" y="660" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Đổi ngoặc tròn thành vuông khi lấy hiệu và bù</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 13: Vận dụng - BÀI TOÁN THỰC TẾ (SGK TRANG 18) (TikZ 08)
# =============================================================
s13 = make_svg(make_header("VẬN DỤNG: BÀI TOÁN THỰC TẾ (SGK TRANG 18)", "VẬN DỤNG") + r'''
  <g id="content">
    <!-- Cột trái: Lời giải bài toán -->
    <rect x="50" y="125" width="580" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">BÀI TOÁN THỂ THAO LỚP 10A</text>

    <text x="85" y="225" fill="#0F172A" font-size="28" font-weight="600">Lớp 10A có 24 bạn thi đấu thể thao:</text>
    <text x="85" y="270" fill="#1E40AF" font-size="28" font-weight="700">• Bóng đá: 16 bạn  |  Cầu lông: 11 bạn.</text>
    <text x="85" y="315" fill="#B91C1C" font-size="30" font-weight="800">Hỏi: Có bao nhiêu bạn thi cả 2 môn?</text>

    <line x1="85" y1="345" x2="590" y2="345" stroke="#E2E8F0" stroke-width="2"/>

    <text x="85" y="390" fill="#047857" font-size="30" font-weight="800">CÔNG THỨC SỐ PHẦN TỬ:</text>
    <rect x="85" y="415" width="510" height="80" rx="14" fill="#FEF3C7" stroke="#FDE68A" stroke-width="2"/>
    <text x="340" y="465" fill="#B45309" font-size="28" font-weight="800" text-anchor="middle"><tspan data-pptx-inline-formula="n(A \cup B) = n(A) + n(B) - n(A \cap B)">n(A ∪ B) = n(A) + n(B) - n(A ∩ B)</tspan></text>

    <text x="85" y="540" fill="#0F172A" font-size="28" font-weight="700">Suy ra: <tspan data-pptx-inline-formula="n(A \cap B) = 16 + 11 - 24 = 3">n(A ∩ B) = 16 + 11 - 24 = 3</tspan></text>
    <text x="85" y="605" fill="#047857" font-size="34" font-weight="800">⇒ Kết quả: Có 3 bạn thi cả 2 môn!</text>

    <!-- Cột phải: TikZ 08 Biểu đồ Ven thể thao -->
    <rect x="650" y="125" width="580" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="940" y="175" fill="#047857" font-size="30" font-weight="800" text-anchor="middle">BIỂU ĐỒ VEN PHÂN BỔ HỌC SINH</text>
    <image href="../images/tikz_08_the_thao.png" x="670" y="200" width="540" height="345" preserveAspectRatio="xMidYMid meet"/>
    <rect x="675" y="565" width="530" height="85" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="940" y="618" fill="#0F172A" font-size="28" font-weight="700" text-anchor="middle">Tổng kiểm tra: 13 + 3 + 8 = 24 bạn</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 14: Tổng kết & Dặn dò (SGK Mục kết bài)
# =============================================================
s14 = make_svg(make_header("TỔNG KẾT BÀI HỌC VÀ NHIỆM VỤ VỀ NHÀ", "TỔNG KẾT") + r'''
  <g id="content">
    <rect x="50" y="125" width="670" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">4 GHI NHỚ TRỌNG TÂM THEO SGK</text>

    <g transform="translate(85, 200)">
      <text x="0" y="40" fill="#0F172A" font-size="28" font-weight="700">1. Mục 1:</text>
      <text x="170" y="40" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="A \subset B">A ⊂ B</tspan> | <tspan data-pptx-inline-formula="A = B">A = B</tspan> (Tập con, bằng nhau)</text>

      <line x1="0" y1="75" x2="600" y2="75" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="125" fill="#0F172A" font-size="28" font-weight="700">2. Mục 2:</text>
      <text x="170" y="125" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="\mathbb{N}^* \subset \mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}">ℕ* ⊂ ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ</tspan></text>

      <line x1="0" y1="160" x2="600" y2="160" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="210" fill="#0F172A" font-size="28" font-weight="700">3. Mục 3:</text>
      <text x="170" y="210" fill="#047857" font-size="28" font-weight="800">Giao <tspan data-pptx-inline-formula="\cap">∩</tspan>, Hợp <tspan data-pptx-inline-formula="\cup">∪</tspan>, Hiệu <tspan data-pptx-inline-formula="\setminus">\</tspan>, Phần bù <tspan data-pptx-inline-formula="C_E A">C_E A</tspan></text>

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
    ("04_tap_con_va_bang_nhau.svg", s04),
    ("05_cac_tap_hop_so.svg", s05),
    ("06_khoang_va_doan.svg", s06),
    ("07_nua_khoang_va_vo_cuc.svg", s07),
    ("08_phep_giao.svg", s08),
    ("09_phep_hop.svg", s09),
    ("10_phep_hieu_va_phan_bu.svg", s10),
    ("11_luyen_tap_de_bai.svg", s11),
    ("12_luyen_tap_loi_giai.svg", s12),
    ("13_van_dung_thuc_te.svg", s13),
    ("14_tong_ket_nhiem_vu.svg", s14)
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

# Clean old SVGs in svg_out_dir to prevent stale pages
for old_f in os.listdir(svg_out_dir):
    if old_f.endswith(".svg"):
        os.remove(os.path.join(svg_out_dir, old_f))

for filename, content in slides:
    filepath = os.path.join(svg_out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated (font >= 28, native equation, SGK sequence): {filepath}")

# Update Notes for 14 slides
notes_content = {
    "01_cover.md": "Kính chào quý thầy cô và các em học sinh. Hôm nay chúng ta cùng học Bài 2: Tập hợp và các phép toán trên tập hợp.",
    "02_muc_tieu.md": "Tiết học này giúp các em nắm vững khái niệm tập con, các tập hợp số, thực hiện thành thạo phép giao, hợp, hiệu và biểu diễn chuẩn trên trục số.",
    "03_khai_niem_tap_hop.md": "Mục 1.a: Khái niệm cơ bản về tập hợp. Các em chú ý hai cách mô tả: liệt kê phần tử hoặc nêu tính chất đặc trưng, cùng khái niệm tập rỗng.",
    "04_tap_con_va_bang_nhau.md": "Mục 1.b và 1.c: Định nghĩa tập hợp con khi mọi phần tử của A đều thuộc B. Biểu đồ Ven minh họa trực quan hình tròn A nằm trọn trong B.",
    "05_cac_tap_hop_so.md": "Mục 2.a: Mối quan hệ giữa các tập hợp số. Chuỗi bao hàm từ số tự nhiên, số nguyên, số hữu tỉ tới số thực R và số vô tỉ I.",
    "06_khoang_va_doan.md": "Mục 2.b Phần 1: Khoảng và Đoạn. Điểm khác biệt mấu chốt: Đoạn [a; b] lấy cả hai đầu mút (dùng ngoặc vuông), Khoảng (a; b) bỏ cả hai mút (dùng ngoặc tròn).",
    "07_nua_khoang_va_vo_cuc.md": "Mục 2.b Phần 2: Nửa khoảng và Khoảng vô cực. Ghi nhớ quy tắc sư phạm: lấy mút dùng ngoặc vuông, bỏ mút dùng ngoặc tròn, gạch chéo phần ngoài.",
    "08_phep_giao.md": "Mục 3.a: Phép giao lấy các phần tử thuộc cả A VÀ B. Biểu đồ Ven biểu thị vùng giao nhau được tô đậm.",
    "09_phep_hop.md": "Mục 3.b: Phép hợp gộp tất cả phần tử thuộc A HOẶC B. Không lặp lại phần tử giống nhau.",
    "10_phep_hieu_va_phan_bu.md": "Mục 3.c: Phép hiệu thuộc A nhưng không thuộc B. Khi A là tập con của E, hiệu E trừ A được gọi là phần bù của A trong E.",
    "11_luyen_tap_de_bai.md": "Luyện tập: Bài tập 1.15 SGK trang 19. Các em có 5 phút vẽ trục số và tìm các kết quả vào vở.",
    "12_luyen_tap_loi_giai.md": "Hướng dẫn giải chi tiết bài 1.15: Lưu ý điểm 1 không thuộc B nên 1 thuộc hiệu A trừ B, chuyển thành ngoặc vuông.",
    "13_van_dung_thuc_te.md": "Vận dụng bài toán thể thao SGK trang 18: Áp dụng công thức số phần tử hợp bằng tổng hai tập trừ giao, tìm ra 3 bạn chơi cả hai môn.",
    "14_tong_ket_nhiem_vu.md": "Tổng kết: 4 ghi nhớ then chốt theo đúng 3 mục của bài học và nhiệm vụ về nhà làm bài 1.8 đến 1.16."
}

for note_f, text in notes_content.items():
    with open(os.path.join(notes_dir, note_f), "w", encoding="utf-8") as f:
        f.write(text)

print("All 14 slides and notes generated strictly following SGK sequence!")
