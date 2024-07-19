import qrcode

# QRコードにエンコードしたいデータを指定
data = "file:///C:/Users/shuni/OneDrive%20-%20%E5%A4%A7%E9%98%AA%E5%B7%A5%E6%A5%AD%E5%A4%A7%E5%AD%A6/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E6%BC%94%E7%BF%92%E2%85%A1/kawakami/kawa.html"

# QRコードのオブジェクトを作成
qr = qrcode.QRCode(
    version=1,  # バージョン: QRコードのサイズを制御
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # エラー訂正レベル
    box_size=10,  # 各ボックスのサイズ
    border=4,  # QRコードのボーダーサイズ
)

# データをQRコードに追加
qr.add_data(data)
qr.make(fit=True)

# 画像を生成
img = qr.make_image(fill_color="black", back_color="white")

# 画像を保存
img.save("qrcode.png")
