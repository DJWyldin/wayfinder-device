def detect(frame):
    # Fake detections for now
    return [
        {"label": "person", "position": "center", "distance": "near"},
        {"label": "chair", "position": "left", "distance": "medium"},
    ]