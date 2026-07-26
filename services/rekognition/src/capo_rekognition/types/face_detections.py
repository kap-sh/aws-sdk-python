"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceDetections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.face_detection

FaceDetections: TypeAlias = list["capo_rekognition.types.face_detection.FaceDetection"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceDetections) -> list:
    import capo_rekognition.types.face_detection

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.face_detection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FaceDetections:
    import capo_rekognition.types.face_detection

    out: FaceDetections = []
    for item in data:
        out.append(capo_rekognition.types.face_detection.deserialize_aws_json_1_1(item))
    return out
