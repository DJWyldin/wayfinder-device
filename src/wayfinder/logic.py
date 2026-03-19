def decide(detections):
    for d in detections:
        label = d["label"]
        pos = d["position"]
        dist = d["distance"]

        if label == "person" and pos == "center":
            return "person ahead"

        if label == "chair" and pos == "left":
            return "chair left"

        if label == "chair" and pos == "right":
            return "chair right"

        if dist == "near":
            return f"{label} close"

    return None