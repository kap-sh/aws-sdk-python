"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceDetection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_detail
    import aws_sdk_rekognition.types.timestamp


class FaceDetection(TypedDict):
    timestamp: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>Time, in milliseconds from the start of the video, that the face was detected. Note that <code>Timestamp</code> is not guaranteed to be accurate to the individual frame where the face first appears.</p>"""
    face: NotRequired["aws_sdk_rekognition.types.face_detail.FaceDetail"]
    """<p>The face properties for the detected face.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceDetection) -> dict:
    out: dict = {}
    out["Timestamp"] = value.get("timestamp", 0)
    if "face" in value:
        import aws_sdk_rekognition.types.face_detail

        out["Face"] = aws_sdk_rekognition.types.face_detail.serialize_aws_json_1_1(
            value["face"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FaceDetection:
    out: FaceDetection = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    else:
        out["timestamp"] = 0
    if "Face" in data:
        import aws_sdk_rekognition.types.face_detail

        out["face"] = aws_sdk_rekognition.types.face_detail.deserialize_aws_json_1_1(
            data["Face"]
        )
    return out
