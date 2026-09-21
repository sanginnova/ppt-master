import os
import re
import sys

project_dir = r"D:\TOAN\ppt-master\projects\bai1_toan12_don_dieu_cuc_tri_20260921"
svg_out_dir = os.path.join(project_dir, "svg_output")
notes_dir = os.path.join(project_dir, "notes")
os.makedirs(svg_out_dir, exist_ok=True)
os.makedirs(notes_dir, exist_ok=True)

# Strict check: font-size >= 28pt across ALL slides
def make_svg(content, lang="vi-VN"):
    lang_attr = f' lang="{lang}"' if lang else ''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"{lang_attr} font-family="Arial, 'Segoe UI', sans-serif">
  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#F8FAFC"/>
  <rect x="0" y="0" width="1280" height="10" fill="#2563EB"/>
{content}
</svg>'''

def make_header(title, tag="TOÁN 12"):
    return f'''  <!-- Header Banner (Cỡ chữ >= 28) -->
  <g id="header-group">
    <rect x="50" y="25" width="1180" height="75" rx="14" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="50" y="25" width="8" height="75" rx="4" fill="#2563EB"/>
    
    <!-- Tag badge -->
    <rect x="75" y="38" width="135" height="48" rx="10" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="142" y="72" fill="#1D4ED8" font-size="28" font-weight="800" text-anchor="middle">{tag}</text>
    
    <!-- Title -->
    <text x="230" y="73" fill="#0F172A" font-size="30" font-weight="800">{title}</text>
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

    <rect x="110" y="155" width="220" height="46" rx="10" fill="#DBEAFE"/>
    <text x="220" y="188" fill="#1E40AF" font-size="28" font-weight="800" text-anchor="middle">CHƯƠNG I - GIẢI TÍCH</text>

    <text x="110" y="260" fill="#0F172A" font-size="44" font-weight="800">BÀI 1. TÍNH ĐƠN ĐIỆU VÀ CỰC TRỊ</text>
    <text x="110" y="320" fill="#2563EB" font-size="44" font-weight="800">CỦA HÀM SỐ</text>
    <text x="110" y="380" fill="#475569" font-size="28" font-weight="600">Toán 12 — Sách Kết nối tri thức với cuộc sống</text>

    <rect x="110" y="425" width="460" height="60" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="340" y="465" fill="#0F172A" font-size="28" font-weight="700" text-anchor="middle">I. Tính đơn điệu của hàm số</text>

    <rect x="600" y="425" width="520" height="60" rx="12" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="860" y="465" fill="#0F172A" font-size="28" font-weight="700" text-anchor="middle">II. Cực trị của hàm số</text>

    <rect x="110" y="520" width="1010" height="110" rx="16" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="150" y="565" fill="#1E3A8A" font-size="30" font-weight="800">Giảng viên: ThS. Nguyễn Văn Sang</text>
    <text x="150" y="605" fill="#475569" font-size="28" font-weight="600">Khoa Cơ bản — Tiết PPCT: 01 - 02</text>
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
    <text x="90" y="220" fill="#0F172A" font-size="28" font-weight="600">• Mối liên hệ giữa dấu của đạo hàm <tspan data-pptx-inline-formula="f'(x)">f'(x)</tspan> và tính đơn điệu của hàm số.</text>
    <text x="90" y="262" fill="#0F172A" font-size="28" font-weight="600">• Khái niệm cực đại, cực tiểu và định lý đổi dấu đạo hàm.</text>

    <rect x="50" y="310" width="1180" height="160" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="50" y="310" width="12" height="160" rx="6" fill="#059669"/>
    <text x="90" y="360" fill="#047857" font-size="30" font-weight="800">2. KỸ NĂNG CẦN ĐẠT</text>
    <text x="90" y="405" fill="#0F172A" font-size="28" font-weight="600">• Thành thạo lập bảng biến thiên để kết luận các khoảng đồng biến, nghịch biến.</text>
    <text x="90" y="447" fill="#0F172A" font-size="28" font-weight="600">• Xác định chính xác các điểm cực trị và giá trị cực trị của hàm số.</text>

    <rect x="50" y="495" width="1180" height="175" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <rect x="50" y="495" width="12" height="175" rx="6" fill="#D97706"/>
    <text x="90" y="545" fill="#B45309" font-size="30" font-weight="800">3. VẬN DỤNG &amp; NĂNG LỰC SỐ</text>
    <text x="90" y="590" fill="#0F172A" font-size="28" font-weight="600">• Ứng dụng đạo hàm giải quyết bài toán chuyển động, tối ưu trong thực tiễn.</text>
    <text x="90" y="632" fill="#0F172A" font-size="28" font-weight="600">• Rèn luyện tư duy biện luận logic và kỹ năng đọc đồ thị hàm số.</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 03: I.a. Khái niệm tính đơn điệu (TikZ 01 Đồ thị)
# =============================================================
s03 = make_svg(make_header("I. TÍNH ĐƠN ĐIỆU: a. Khái niệm tính đơn điệu", "MỤC I.a") + r'''
  <g id="content">
    <rect x="50" y="125" width="560" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    
    <g transform="translate(80, 155)">
      <!-- Dong bien -->
      <rect x="0" y="0" width="500" height="210" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
      <text x="20" y="45" fill="#1D4ED8" font-size="30" font-weight="800">1. HÀM SỐ ĐỒNG BIẾN (TĂNG):</text>
      <text x="20" y="90" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="\forall x_1, x_2 \in K: x_1 &lt; x_2 \Rightarrow f(x_1) &lt; f(x_2)">∀x₁, x₂ ∈ K: x₁ &lt; x₂ ⇒ f(x₁) &lt; f(x₂)</tspan></text>
      <text x="20" y="135" fill="#1E40AF" font-size="28" font-weight="700">Đặc trưng hình học đồ thị:</text>
      <text x="20" y="175" fill="#047857" font-size="28" font-weight="800">→ ĐỒ THỊ ĐI LÊN TỪ TRÁI SANG PHẢI</text>

      <!-- Nghich bien -->
      <rect x="0" y="235" width="500" height="210" rx="14" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
      <text x="20" y="280" fill="#DC2626" font-size="30" font-weight="800">2. HÀM SỐ NGHỊCH BIẾN (GIẢM):</text>
      <text x="20" y="325" fill="#0F172A" font-size="28" font-weight="600"><tspan data-pptx-inline-formula="\forall x_1, x_2 \in K: x_1 &lt; x_2 \Rightarrow f(x_1) &gt; f(x_2)">∀x₁, x₂ ∈ K: x₁ &lt; x₂ ⇒ f(x₁) &gt; f(x₂)</tspan></text>
      <text x="20" y="370" fill="#B91C1C" font-size="28" font-weight="700">Đặc trưng hình học đồ thị:</text>
      <text x="20" y="410" fill="#B91C1C" font-size="28" font-weight="800">→ ĐỒ THỊ ĐI XUỐNG TỪ TRÁI SANG PHẢI</text>
    </g>

    <!-- Cot phai: TikZ 01 Do thi dong bien & nghich bien -->
    <rect x="630" y="125" width="600" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="930" y="170" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">HÌNH DÁNG ĐỒ THỊ (HÌNH 1.2 SGK)</text>
    <image href="../images/tikz_01_do_thi_don_dieu.png" x="650" y="190" width="560" height="420" preserveAspectRatio="xMidYMid meet"/>
    <text x="930" y="645" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">K là một khoảng, đoạn hoặc nửa khoảng</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 04: I. Định lý đạo hàm & Tính đơn điệu (SGK Trang 6)
# =============================================================
s04 = make_svg(make_header("I. TÍNH ĐƠN ĐIỆU: Định lý đạo hàm &amp; Tính đơn điệu", "ĐỊNH LÝ") + r'''
  <g id="content">
    <rect x="50" y="125" width="1180" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    
    <rect x="85" y="155" width="1110" height="95" rx="14" fill="#EFF6FF" stroke="#2563EB" stroke-width="2"/>
    <text x="110" y="200" fill="#1E40AF" font-size="30" font-weight="800">ĐỊNH LÝ CỐT LÕI (SGK TOÁN 12 - TRANG 6):</text>
    <text x="110" y="235" fill="#0F172A" font-size="28" font-weight="600">Cho hàm số <tspan data-pptx-inline-formula="y = f(x)">y = f(x)</tspan> có đạo hàm trên khoảng <tspan data-pptx-inline-formula="K">K</tspan>:</text>

    <g transform="translate(85, 275)">
      <!-- Truong hop 1: f'(x) > 0 -->
      <rect x="0" y="0" width="540" height="150" rx="14" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="2"/>
      <text x="25" y="45" fill="#047857" font-size="30" font-weight="800">1. ĐẠO HÀM MANG DẤU DƯƠNG:</text>
      <text x="25" y="90" fill="#0F172A" font-size="28" font-weight="600">Nếu <tspan data-pptx-inline-formula="f'(x) &gt; 0, \forall x \in K">f'(x) &gt; 0, ∀x ∈ K</tspan> thì:</text>
      <text x="25" y="130" fill="#166534" font-size="30" font-weight="800">⇒ Hàm số <tspan data-pptx-inline-formula="f(x)">f(x)</tspan> ĐỒNG BIẾN trên <tspan data-pptx-inline-formula="K">K</tspan></text>

      <!-- Truong hop 2: f'(x) < 0 -->
      <rect x="570" y="0" width="540" height="150" rx="14" fill="#FEF2F2" stroke="#FECACA" stroke-width="2"/>
      <text x="595" y="45" fill="#DC2626" font-size="30" font-weight="800">2. ĐẠO HÀM MANG DẤU ÂM:</text>
      <text x="595" y="90" fill="#0F172A" font-size="28" font-weight="600">Nếu <tspan data-pptx-inline-formula="f'(x) &lt; 0, \forall x \in K">f'(x) &lt; 0, ∀x ∈ K</tspan> thì:</text>
      <text x="595" y="130" fill="#B91C1C" font-size="30" font-weight="800">⇒ Hàm số <tspan data-pptx-inline-formula="f(x)">f(x)</tspan> NGHỊCH BIẾN trên <tspan data-pptx-inline-formula="K">K</tspan></text>
    </g>

    <!-- Chu y mo rong -->
    <rect x="85" y="455" width="1110" height="195" rx="14" fill="#FFFBEB" stroke="#FDE68A" stroke-width="2"/>
    <text x="115" y="500" fill="#B45309" font-size="30" font-weight="800">📌 CHÚ Ý MỞ RỘNG VÀ QUY TẮC DẤU BẰNG:</text>
    <text x="115" y="545" fill="#0F172A" font-size="28" font-weight="600">• Định lý vẫn đúng khi <tspan data-pptx-inline-formula="f'(x) = 0">f'(x) = 0</tspan> tại một số hữu hạn điểm trên khoảng <tspan data-pptx-inline-formula="K">K</tspan>.</text>
    <text x="115" y="588" fill="#0F172A" font-size="28" font-weight="600">• Nếu <tspan data-pptx-inline-formula="f'(x) = 0, \forall x \in K">f'(x) = 0, ∀x ∈ K</tspan> thì hàm số <tspan data-pptx-inline-formula="f(x)">f(x)</tspan> là hàm hằng (không đổi trên K).</text>
    <text x="115" y="630" fill="#1E40AF" font-size="28" font-weight="700">Dấu của đạo hàm quyết định hoàn toàn chiều biến thiên của đồ thị!</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 05: I.b. Quy trình xét đơn điệu qua BBT (TikZ 02 BBT)
# =============================================================
s05 = make_svg(make_header("I. TÍNH ĐƠN ĐIỆU: b. Quy trình xét qua Bảng biến thiên", "MỤC I.b") + r'''
  <g id="content">
    <!-- Cot trai: 4 buoc xet tinh don dieu -->
    <rect x="50" y="125" width="560" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">4 BƯỚC XÉT ĐƠN ĐIỆU CHUẨN SGK</text>

    <g transform="translate(85, 205)">
      <rect x="0" y="0" width="490" height="95" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
      <text x="20" y="40" fill="#1E40AF" font-size="28" font-weight="800">BƯỚC 1: Tìm tập xác định (TXĐ)</text>
      <text x="20" y="78" fill="#0F172A" font-size="28" font-weight="600">Tìm tập xác định D của hàm số.</text>

      <rect x="0" y="110" width="490" height="105" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
      <text x="20" y="150" fill="#1E40AF" font-size="28" font-weight="800">BƯỚC 2: Tính đạo hàm <tspan data-pptx-inline-formula="y' = f'(x)">y' = f'(x)</tspan></text>
      <text x="20" y="192" fill="#0F172A" font-size="28" font-weight="600">Tìm các điểm <tspan data-pptx-inline-formula="x_i">x_i</tspan> mà <tspan data-pptx-inline-formula="f'(x_i) = 0">f'(x_i) = 0</tspan> hoặc ko xác định.</text>

      <rect x="0" y="230" width="490" height="105" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
      <text x="20" y="270" fill="#1E40AF" font-size="28" font-weight="800">BƯỚC 3: Lập Bảng biến thiên (BBT)</text>
      <text x="20" y="312" fill="#0F172A" font-size="28" font-weight="600">Sắp xếp <tspan data-pptx-inline-formula="x_i">x_i</tspan> tăng dần, xét dấu <tspan data-pptx-inline-formula="f'(x)">f'(x)</tspan>.</text>

      <rect x="0" y="350" width="490" height="95" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
      <text x="20" y="390" fill="#047857" font-size="28" font-weight="800">BƯỚC 4: Kết luận các khoảng</text>
      <text x="20" y="428" fill="#166534" font-size="28" font-weight="700">Chỉ ra khoảng đồng biến, nghịch biến.</text>
    </g>

    <!-- Cot phai: TikZ 02 Bảng biến thiên chuẩn -->
    <rect x="630" y="125" width="600" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="930" y="170" fill="#047857" font-size="30" font-weight="800" text-anchor="middle">MẪU BẢNG BIẾN THIÊN CHUẨN</text>
    <image href="../images/tikz_02_bbt_don_dieu.png" x="650" y="210" width="560" height="260" preserveAspectRatio="xMidYMid meet"/>

    <rect x="650" y="500" width="560" height="145" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
    <text x="670" y="545" fill="#1E40AF" font-size="28" font-weight="800">ĐỌC KẾT QUẢ TỪ BẢNG BIẾN THIÊN:</text>
    <text x="670" y="585" fill="#0F172A" font-size="28" font-weight="600">• Đồng biến trên: <tspan data-pptx-inline-formula="(-\infty; -1)">(-∞; -1)</tspan> và <tspan data-pptx-inline-formula="(2; +\infty)">(2; +∞)</tspan></text>
    <text x="670" y="625" fill="#DC2626" font-size="28" font-weight="700">• Nghịch biến trên khoảng: <tspan data-pptx-inline-formula="(-1; 2)">(-1; 2)</tspan></text>
  </g>
''', lang="")

# =============================================================
# SLIDE 06: II.a. Khái niệm cực trị của hàm số (TikZ 03 Đồ thị)
# =============================================================
s06 = make_svg(make_header("II. CỰC TRỊ: a. Khái niệm cực đại &amp; cực tiểu", "MỤC II.a") + r'''
  <g id="content">
    <rect x="50" y="125" width="620" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">ĐỊNH NGHĨA CỰC TRỊ (SGK TRANG 9)</text>

    <g transform="translate(80, 205)">
      <!-- Cuc dai -->
      <rect x="0" y="0" width="560" height="205" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
      <text x="20" y="45" fill="#1D4ED8" font-size="30" font-weight="800">1. ĐIỂM CỰC ĐẠI (<tspan data-pptx-inline-formula="x_0">x₀</tspan>):</text>
      <text x="20" y="90" fill="#0F172A" font-size="28" font-weight="600">Tồn tại khoảng <tspan data-pptx-inline-formula="(x_0-h; x_0+h)">(x₀-h; x₀+h)</tspan> sao cho:</text>
      <text x="20" y="135" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="f(x) &lt; f(x_0), \forall x \neq x_0">f(x) &lt; f(x₀), ∀x ≠ x₀</tspan></text>
      <text x="20" y="178" fill="#047857" font-size="28" font-weight="800">→ HÌNH ẢNH: ĐỈNH ĐỒI (CAO NHẤT LÂN CẬN)</text>

      <!-- Cuc tieu -->
      <rect x="0" y="225" width="560" height="205" rx="14" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
      <text x="20" y="270" fill="#DC2626" font-size="30" font-weight="800">2. ĐIỂM CỰC TIỂU (<tspan data-pptx-inline-formula="x_0">x₀</tspan>):</text>
      <text x="20" y="315" fill="#0F172A" font-size="28" font-weight="600">Tồn tại khoảng <tspan data-pptx-inline-formula="(x_0-h; x_0+h)">(x₀-h; x₀+h)</tspan> sao cho:</text>
      <text x="20" y="360" fill="#B91C1C" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="f(x) &gt; f(x_0), \forall x \neq x_0">f(x) &gt; f(x₀), ∀x ≠ x₀</tspan></text>
      <text x="20" y="403" fill="#B91C1C" font-size="28" font-weight="800">→ HÌNH ẢNH: ĐÁY THUNG LŨNG (THẤP NHẤT)</text>
    </g>

    <!-- Cot phai: TikZ 03 Do thi Dinh doi & Day thung lung -->
    <rect x="690" y="125" width="540" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="960" y="170" fill="#1E40AF" font-size="30" font-weight="800" text-anchor="middle">MINH HỌA TRỰC QUAN ĐỒ THỊ</text>
    <image href="../images/tikz_03_minh_hoa_cuc_tri.png" x="710" y="190" width="500" height="425" preserveAspectRatio="xMidYMid meet"/>
    <text x="960" y="645" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Cực trị chỉ có tính chất địa phương (lân cận)</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 07: II. Phân biệt các khái niệm Cực trị (Native Equation)
# =============================================================
s07 = make_svg(make_header("II. CỰC TRỊ: Phân biệt 3 khái niệm cốt lõi", "QUY TẮC") + r'''
  <g id="content">
    <rect x="50" y="125" width="1180" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    
    <rect x="85" y="155" width="1110" height="80" rx="12" fill="#FEF3C7" stroke="#FDE68A" stroke-width="2"/>
    <text x="110" y="205" fill="#92400E" font-size="30" font-weight="800">⚠️ LƯU Ý SƯ PHẠM: HỌC SINH RẤT DỄ NHẦM LẪN 3 KHÁI NIỆM NÀY!</text>

    <g transform="translate(85, 260)">
      <!-- 1. Diem cuc tri ham so -->
      <rect x="0" y="0" width="350" height="230" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="2"/>
      <text x="25" y="45" fill="#1D4ED8" font-size="30" font-weight="800">1. ĐIỂM CỰC TRỊ</text>
      <text x="25" y="85" fill="#1E40AF" font-size="28" font-weight="800">CỦA HÀM SỐ:</text>
      <text x="25" y="135" fill="#0F172A" font-size="30" font-weight="700">Chính là hoành độ:</text>
      <text x="25" y="180" fill="#1D4ED8" font-size="36" font-weight="800"><tspan data-pptx-inline-formula="x_0">x₀</tspan> (<tspan data-pptx-inline-formula="x_{CĐ}">x_{CĐ}</tspan>, <tspan data-pptx-inline-formula="x_{CT}">x_{CT}</tspan>)</text>

      <!-- 2. Gia tri cuc tri -->
      <rect x="380" y="0" width="350" height="230" rx="14" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="2"/>
      <text x="405" y="45" fill="#047857" font-size="30" font-weight="800">2. GIÁ TRỊ CỰC TRỊ</text>
      <text x="405" y="85" fill="#065F46" font-size="28" font-weight="800">(CỰC TRỊ HÀM SỐ):</text>
      <text x="405" y="135" fill="#0F172A" font-size="30" font-weight="700">Chính là tung độ:</text>
      <text x="405" y="180" fill="#047857" font-size="36" font-weight="800"><tspan data-pptx-inline-formula="y_0 = f(x_0)">y₀ = f(x₀)</tspan></text>

      <!-- 3. Diem cuc tri do thi -->
      <rect x="760" y="0" width="350" height="230" rx="14" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="2"/>
      <text x="785" y="45" fill="#7C3AED" font-size="30" font-weight="800">3. ĐIỂM CỰC TRỊ</text>
      <text x="785" y="85" fill="#6B21A8" font-size="28" font-weight="800">CỦA ĐỒ THỊ:</text>
      <text x="785" y="135" fill="#0F172A" font-size="30" font-weight="700">Cặp tọa độ mặt phẳng:</text>
      <text x="785" y="180" fill="#7C3AED" font-size="34" font-weight="800"><tspan data-pptx-inline-formula="M(x_0; y_0)">M(x₀; y₀)</tspan></text>
    </g>

    <rect x="85" y="520" width="1110" height="125" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="115" y="565" fill="#0F172A" font-size="28" font-weight="700">Ví dụ hàm số có điểm cực đại <tspan data-pptx-inline-formula="x = 1">x = 1</tspan> và giá trị <tspan data-pptx-inline-formula="f(1) = 4">f(1) = 4</tspan>:</text>
    <text x="115" y="615" fill="#1E40AF" font-size="30" font-weight="800">→ Điểm CĐ là <tspan data-pptx-inline-formula="x = 1">x = 1</tspan> | Giá trị CĐ là <tspan data-pptx-inline-formula="y = 4">y = 4</tspan> | Điểm CĐ đồ thị là <tspan data-pptx-inline-formula="A(1; 4)">A(1; 4)</tspan></text>
  </g>
''', lang="")

# =============================================================
# SLIDE 08: II.b. Định lý đổi dấu đạo hàm (TikZ 04 BBT Đổi dấu)
# =============================================================
s08 = make_svg(make_header("II. CỰC TRỊ: b. Định lý đổi dấu đạo hàm", "MỤC II.b") + r'''
  <g id="content">
    <rect x="50" y="125" width="1180" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">ĐỊNH LÝ DẤU HIỆU CỰC TRỊ (SGK TRANG 10)</text>

    <!-- TikZ 04 Bang doi dau f' -->
    <image href="../images/tikz_04_dinh_ly_doi_dau_fphay.png" x="85" y="200" width="1110" height="260" preserveAspectRatio="xMidYMid meet"/>

    <g transform="translate(85, 480)">
      <rect x="0" y="0" width="540" height="160" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
      <text x="25" y="45" fill="#1D4ED8" font-size="30" font-weight="800">QUY TẮC CỰC ĐẠI:</text>
      <text x="25" y="90" fill="#0F172A" font-size="28" font-weight="600">Đạo hàm đổi dấu từ <tspan data-pptx-inline-formula="(+)">dương (+)</tspan> sang <tspan data-pptx-inline-formula="(-)">âm (-)</tspan></text>
      <text x="25" y="135" fill="#1E40AF" font-size="28" font-weight="800">→ Hàm số đạt CỰC ĐẠI tại <tspan data-pptx-inline-formula="x_0">x₀</tspan></text>

      <rect x="570" y="0" width="540" height="160" rx="14" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
      <text x="595" y="45" fill="#DC2626" font-size="30" font-weight="800">QUY TẮC CỰC TIỂU:</text>
      <text x="595" y="90" fill="#0F172A" font-size="28" font-weight="600">Đạo hàm đổi dấu từ <tspan data-pptx-inline-formula="(-)">âm (-)</tspan> sang <tspan data-pptx-inline-formula="(+)">dương (+)</tspan></text>
      <text x="595" y="135" fill="#B91C1C" font-size="28" font-weight="800">→ Hàm số đạt CỰC TIỂU tại <tspan data-pptx-inline-formula="x_0">x₀</tspan></text>
    </g>
  </g>
''', lang="")

# =============================================================
# SLIDE 09: Luyện tập - BÀI TOÁN XÉT BIẾN THIÊN & CỰC TRỊ (ĐỀ BÀI)
# =============================================================
s09 = make_svg(make_header("BÀI TẬP VẬN DỤNG KIẾN THỨC BÀI 1", "LUYỆN TẬP") + r'''
  <g id="exercise-content">
    <rect x="50" y="125" width="1180" height="545" rx="20" fill="#FFFFFF" stroke="#3B82F6" stroke-width="3"/>
    
    <rect x="80" y="155" width="1120" height="150" rx="14" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="2"/>
    <text x="110" y="205" fill="#1D4ED8" font-size="32" font-weight="800">ĐỀ BÀI (ÁP DỤNG QUY TRÌNH 4 BƯỚC):</text>
    <text x="110" y="260" fill="#0F172A" font-size="34" font-weight="800">Cho hàm số:  <tspan data-pptx-inline-formula="y = x^3 - 3x^2 + 2">y = x³ - 3x² + 2</tspan></text>

    <g transform="translate(80, 335)">
      <rect x="0" y="0" width="545" height="105" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="30" y="48" fill="#1D4ED8" font-size="30" font-weight="800">Câu a)  Tính đạo hàm <tspan data-pptx-inline-formula="y'">y'</tspan> và giải <tspan data-pptx-inline-formula="y' = 0">y' = 0</tspan></text>
      <text x="30" y="88" fill="#475569" font-size="28">Tìm các nghiệm thực của phương trình đạo hàm.</text>

      <rect x="575" y="0" width="545" height="105" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="605" y="48" fill="#047857" font-size="30" font-weight="800">Câu b)  Lập bảng biến thiên</text>
      <text x="605" y="88" fill="#475569" font-size="28">Xét dấu đạo hàm và điền các giá trị cực trị.</text>

      <rect x="0" y="130" width="1120" height="75" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="30" y="178" fill="#B45309" font-size="30" font-weight="800">Câu c)  Kết luận các khoảng đơn điệu và các điểm cực trị của hàm số</text>
    </g>

    <rect x="80" y="570" width="1120" height="75" rx="14" fill="#FEF2F2" stroke="#FECACA" stroke-width="2"/>
    <text x="640" y="618" fill="#991B1B" font-size="30" font-weight="800" text-anchor="middle">⏱ CẢ LỚP LÀM VÀO VỞ TRONG 5 PHÚT — THỰC HIỆN ĐỦ 4 BƯỚC!</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 10: Luyện tập - HƯỚNG DẪN GIẢI CHI TIẾT (TikZ 05 BBT)
# =============================================================
s10 = make_svg(make_header("HƯỚNG DẪN GIẢI CHI TIẾT BÀI TẬP VẬN DỤNG", "LỜI GIẢI") + r'''
  <g id="solution-content">
    <rect x="50" y="125" width="560" height="545" rx="20" fill="#FFFFFF" stroke="#10B981" stroke-width="3"/>
    
    <g transform="translate(75, 145)">
      <rect x="0" y="0" width="510" height="105" rx="12" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
      <text x="20" y="42" fill="#1E40AF" font-size="28" font-weight="800">1. TXĐ &amp; Đạo hàm:</text>
      <text x="20" y="85" fill="#0F172A" font-size="28" font-weight="700"><tspan data-pptx-inline-formula="D = \mathbb{R}">D = ℝ</tspan> | <tspan data-pptx-inline-formula="y' = 3x^2 - 6x = 3x(x - 2)">y' = 3x² - 6x = 3x(x - 2)</tspan></text>

      <rect x="0" y="120" width="510" height="95" rx="12" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5"/>
      <text x="20" y="160" fill="#1E40AF" font-size="28" font-weight="800">2. Nghiệm đạo hàm:</text>
      <text x="20" y="198" fill="#1D4ED8" font-size="30" font-weight="800"><tspan data-pptx-inline-formula="y' = 0 \Leftrightarrow x = 0">y' = 0 ⇔ x = 0</tspan> hoặc <tspan data-pptx-inline-formula="x = 2">x = 2</tspan></text>

      <rect x="0" y="230" width="510" height="110" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="1.5"/>
      <text x="20" y="270" fill="#047857" font-size="28" font-weight="800">3. Khoảng đơn điệu:</text>
      <text x="20" y="308" fill="#166534" font-size="28" font-weight="700">• Đồng biến: <tspan data-pptx-inline-formula="( -\infty; 0 )">(-∞; 0)</tspan> và <tspan data-pptx-inline-formula="( 2; +\infty )">(2; +∞)</tspan></text>
      <text x="20" y="340" fill="#DC2626" font-size="28" font-weight="700">• Nghịch biến trên khoảng: <tspan data-pptx-inline-formula="(0; 2)">(0; 2)</tspan></text>

      <rect x="0" y="355" width="510" height="115" rx="12" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
      <text x="20" y="395" fill="#7C3AED" font-size="28" font-weight="800">4. Cực trị hàm số:</text>
      <text x="20" y="432" fill="#6B21A8" font-size="28" font-weight="700">• Điểm CĐ: <tspan data-pptx-inline-formula="x = 0 \Rightarrow y_{CĐ} = 2">x = 0 ⇒ y_{CĐ} = 2</tspan></text>
      <text x="20" y="462" fill="#6B21A8" font-size="28" font-weight="700">• Điểm CT: <tspan data-pptx-inline-formula="x = 2 \Rightarrow y_{CT} = -2">x = 2 ⇒ y_{CT} = -2</tspan></text>
    </g>

    <!-- Cot phai: TikZ 05 BBT loi giai -->
    <rect x="630" y="125" width="600" height="545" rx="20" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="930" y="170" fill="#047857" font-size="30" font-weight="800" text-anchor="middle">BẢNG BIẾN THIÊN HOÀN CHỈNH</text>
    <image href="../images/tikz_05_bbt_loi_giai.png" x="650" y="205" width="560" height="280" preserveAspectRatio="xMidYMid meet"/>
    
    <rect x="650" y="520" width="560" height="125" rx="14" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>
    <text x="670" y="565" fill="#0F172A" font-size="28" font-weight="700">TỌA ĐỘ ĐIỂM CỰC TRỊ CỦA ĐỒ THỊ:</text>
    <text x="670" y="615" fill="#1E40AF" font-size="30" font-weight="800">Điểm CĐ: <tspan data-pptx-inline-formula="A(0; 2)">A(0; 2)</tspan>  |  Điểm CT: <tspan data-pptx-inline-formula="B(2; -2)">B(2; -2)</tspan></text>
  </g>
''', lang="")

# =============================================================
# SLIDE 11: Vận dụng - BÀI TOÁN CHUYỂN ĐỘNG THỰC TẾ (TikZ 06)
# =============================================================
s11 = make_svg(make_header("VẬN DỤNG: ỨNG DỤNG THỰC TẾ TRONG CHUYỂN ĐỘNG", "VẬN DỤNG") + r'''
  <g id="content">
    <!-- Cot trai: De bai va loi giai -->
    <rect x="50" y="125" width="600" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">BÀI TOÁN TỐC ĐỘ RƠI / PHÓNG TÊN LỬA</text>

    <text x="85" y="225" fill="#0F172A" font-size="28" font-weight="600">Vận tốc một vật chuyển động theo thời gian <tspan data-pptx-inline-formula="t">t</tspan>:</text>
    <rect x="85" y="250" width="530" height="75" rx="12" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="350" y="298" fill="#B45309" font-size="30" font-weight="800" text-anchor="middle"><tspan data-pptx-inline-formula="v(t) = -t^2 + 6t + 8">v(t) = -t² + 6t + 8</tspan>  <tspan data-pptx-inline-formula="(t \ge 0)">(t ≥ 0)</tspan></text>

    <text x="85" y="360" fill="#B91C1C" font-size="30" font-weight="800">Hỏi: Tại thời điểm nào vận tốc đạt cực đại?</text>
    
    <line x1="85" y1="390" x2="610" y2="390" stroke="#E2E8F0" stroke-width="2"/>

    <text x="85" y="435" fill="#047857" font-size="30" font-weight="800">ÁP DỤNG ĐẠO HÀM TÌM CỰC TRỊ:</text>
    <text x="85" y="480" fill="#0F172A" font-size="28" font-weight="700">• Gia tốc: <tspan data-pptx-inline-formula="v'(t) = -2t + 6">v'(t) = -2t + 6</tspan></text>
    <text x="85" y="525" fill="#0F172A" font-size="28" font-weight="700">• Giải: <tspan data-pptx-inline-formula="v'(t) = 0 \Leftrightarrow -2t + 6 = 0 \Leftrightarrow t = 3">v'(t) = 0 ⇔ -2t + 6 = 0 ⇔ t = 3</tspan> (giây)</text>

    <rect x="85" y="560" width="530" height="90" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="2"/>
    <text x="105" y="618" fill="#166534" font-size="30" font-weight="800">⇒ Sau 3 giây, vận tốc đạt cực đại <tspan data-pptx-inline-formula="v_{\max} = 17\text{ m/s}">v_{max} = 17 m/s</tspan></text>

    <!-- Cot phai: TikZ 06 Do thi chuyen dong -->
    <rect x="670" y="125" width="560" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="950" y="175" fill="#047857" font-size="30" font-weight="800" text-anchor="middle">ĐỒ THỊ VẬN TỐC THEO THỜI GIAN</text>
    <image href="../images/tikz_06_van_dung_chuyen_dong.png" x="690" y="200" width="520" height="420" preserveAspectRatio="xMidYMid meet"/>
    <text x="950" y="645" fill="#64748B" font-size="28" font-weight="600" text-anchor="middle">Đỉnh parabol biểu thị giá trị cực đại thực tế</text>
  </g>
''', lang="")

# =============================================================
# SLIDE 12: Tổng kết & Dặn dò
# =============================================================
s12 = make_svg(make_header("TỔNG KẾT BÀI HỌC VÀ NHIỆM VỤ VỀ NHÀ", "TỔNG KẾT") + r'''
  <g id="content">
    <rect x="50" y="125" width="670" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="85" y="175" fill="#1D4ED8" font-size="30" font-weight="800">4 GHI NHỚ TRỌNG TÂM BÀI 1</text>

    <g transform="translate(85, 205)">
      <text x="0" y="40" fill="#0F172A" font-size="28" font-weight="700">1. Tính đơn điệu:</text>
      <text x="210" y="40" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="f'(x) &gt; 0">f'(x) &gt; 0</tspan> (Đồng biến), <tspan data-pptx-inline-formula="f'(x) &lt; 0">f'(x) &lt; 0</tspan> (Nghịch biến)</text>

      <line x1="0" y1="75" x2="600" y2="75" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="125" fill="#0F172A" font-size="28" font-weight="700">2. Định lý cực trị:</text>
      <text x="210" y="125" fill="#1E40AF" font-size="28" font-weight="800"><tspan data-pptx-inline-formula="(+) \to (-)">+ qua -</tspan> (Cực đại) | <tspan data-pptx-inline-formula="(-) \to (+)">- qua +</tspan> (Cực tiểu)</text>

      <line x1="0" y1="160" x2="600" y2="160" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="210" fill="#0F172A" font-size="28" font-weight="700">3. Phân biệt 3 k.niệm:</text>
      <text x="210" y="210" fill="#047857" font-size="28" font-weight="800">Điểm cực trị <tspan data-pptx-inline-formula="x_0">x₀</tspan>, Giá trị <tspan data-pptx-inline-formula="y_0">y₀</tspan>, Đồ thị <tspan data-pptx-inline-formula="M(x_0; y_0)">M(x₀; y₀)</tspan></text>

      <line x1="0" y1="245" x2="600" y2="245" stroke="#F1F5F9" stroke-width="2"/>

      <text x="0" y="295" fill="#0F172A" font-size="28" font-weight="700">4. Kỹ năng cốt lõi:</text>
      <text x="210" y="295" fill="#D97706" font-size="28" font-weight="800">Lập thành thạo Bảng biến thiên (BBT)</text>
    </g>

    <rect x="750" y="125" width="480" height="545" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text x="785" y="175" fill="#9333EA" font-size="30" font-weight="800">NHIỆM VỤ VỀ NHÀ</text>

    <rect x="775" y="210" width="430" height="195" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="800" y="260" fill="#0F172A" font-size="28" font-weight="700">• Làm bài 1.1 đến 1.8</text>
    <text x="800" y="305" fill="#64748B" font-size="28">  (SGK Toán 12, trang 11 - 12)</text>
    <text x="800" y="360" fill="#1E40AF" font-size="28" font-weight="700">• Đọc trước Bài 2: GTLN &amp; GTNN</text>

    <rect x="775" y="435" width="430" height="210" rx="16" fill="#0F172A"/>
    <text x="990" y="495" fill="#FFFFFF" font-size="32" font-weight="800" text-anchor="middle">CHÚC CÁC EM</text>
    <text x="990" y="540" fill="#38BDF8" font-size="32" font-weight="800" text-anchor="middle">HỌC TỐT MÔN TOÁN 12!</text>
    <text x="990" y="605" fill="#94A3B8" font-size="28" font-weight="600" text-anchor="middle">Thầy Nguyễn Văn Sang</text>
  </g>
''', lang="")

slides = [
    ("01_cover.svg", s01),
    ("02_muc_tieu.svg", s02),
    ("03_khai_niem_don_dieu.svg", s03),
    ("04_dinh_ly_dao_ham.svg", s04),
    ("05_quy_trinh_bbt.svg", s05),
    ("06_khai_niem_cuc_tri.svg", s06),
    ("07_phan_biet_cuc_tri.svg", s07),
    ("08_dinh_ly_doi_dau.svg", s08),
    ("09_luyen_tap_de_bai.svg", s09),
    ("10_luyen_tap_loi_giai.svg", s10),
    ("11_van_dung_thuc_te.svg", s11),
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

for old_f in os.listdir(svg_out_dir):
    if old_f.endswith(".svg"):
        os.remove(os.path.join(svg_out_dir, old_f))

for filename, content in slides:
    filepath = os.path.join(svg_out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated (font >= 28, native equation, Toan 12 SGK): {filepath}")

# Update Notes for 12 slides
notes_content = {
    "01_cover.md": "Chào mừng các em học sinh đến với chương trình Toán 12. Bài mở đầu Chương I: Tính đơn điệu và cực trị của hàm số.",
    "02_muc_tieu.md": "Tiết học này giúp các em làm chủ mối liên hệ giữa dấu đạo hàm và tính đơn điệu, nắm vững khái niệm cực trị và lập thành thạo bảng biến thiên.",
    "03_khai_niem_don_dieu.md": "Mục I.a: Nhắc lại tính đồng biến khi x tăng thì y tăng (đồ thị đi lên), nghịch biến khi x tăng thì y giảm (đồ thị đi xuống).",
    "04_dinh_ly_dao_ham.md": "Định lý then chốt của Giải tích 12: Đạo hàm mang dấu dương thì hàm số đồng biến; đạo hàm mang dấu âm thì hàm số nghịch biến.",
    "05_quy_trinh_bbt.md": "Quy trình 4 bước lập bảng biến thiên chuẩn SGK: Tìm TXĐ, tính đạo hàm tìm nghiệm, lập bảng biến thiên và kết luận các khoảng.",
    "06_khai_niem_cuc_tri.md": "Mục II.a: Điểm cực đại là đỉnh đồi cao nhất trong lân cận; điểm cực tiểu là đáy thung lũng thấp nhất trong lân cận.",
    "07_phan_biet_cuc_tri.md": "Phân biệt 3 khái niệm: Điểm cực trị hàm số x0, Giá trị cực trị y0, và Điểm cực trị của đồ thị hàm số M(x0; y0).",
    "08_dinh_ly_doi_dau.md": "Mục II.b: Dấu hiệu tìm cực trị qua sự đổi dấu đạo hàm: từ dương sang âm là cực đại, từ âm sang dương là cực tiểu.",
    "09_luyen_tap_de_bai.md": "Luyện tập: Cho hàm bậc ba y = x^3 - 3x^2 + 2. Các em áp dụng quy trình 4 bước làm vào vở trong 5 phút.",
    "10_luyen_tap_loi_giai.md": "Hướng dẫn giải chi tiết: Hàm số có 2 điểm cực trị x = 0 và x = 2. Giá trị cực đại y = 2, giá trị cực tiểu y = -2.",
    "11_van_dung_thuc_te.md": "Vận dụng thực tế: Ứng dụng đạo hàm tìm thời điểm vận tốc cực đại trong chuyển động tên lửa/vật rơi tại t = 3 giây.",
    "12_tong_ket_nhiem_vu.md": "Tổng kết 4 ghi nhớ then chốt của Bài 1 và dặn dò các em hoàn thành bài tập 1.1 đến 1.8 SGK trang 11-12."
}

for note_f, text in notes_content.items():
    with open(os.path.join(notes_dir, note_f), "w", encoding="utf-8") as f:
        f.write(text)

print("All 12 slides and notes for Toan 12 Bai 1 generated successfully!")
