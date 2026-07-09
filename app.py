import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("best1.pt")

while True:
    success, img = cap.read()
    if not success:
        break

    results = model(img, imgsz=320, verbose=False)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            if conf < 0.5:
                continue

            classname = model.names[cls]

            if classname in ["NO-Hardhat", "NO-Mask", "NO-Safety Vest"]:
                color = (0, 0, 255)
            elif classname in ["Hardhat", "Mask", "Safety Vest"]:
                color = (0, 255, 0)
            else:
                color = (255, 0, 0)

            label = f"{classname} {conf:.2f}"

            cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("PPE Detection", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
