"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face
    import aws_sdk_rekognition.types.face_detail


class FaceRecord(TypedDict):
    face: NotRequired["aws_sdk_rekognition.types.face.Face"]
    """<p>Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned. </p>"""
    face_detail: NotRequired["aws_sdk_rekognition.types.face_detail.FaceDetail"]
    """<p>Structure containing attributes of the face that the algorithm detected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceRecord) -> dict:
    out: dict = {}
    if "face" in value:
        import aws_sdk_rekognition.types.face

        out["Face"] = aws_sdk_rekognition.types.face.serialize_aws_json_1_1(
            value["face"]
        )
    if "face_detail" in value:
        import aws_sdk_rekognition.types.face_detail

        out["FaceDetail"] = (
            aws_sdk_rekognition.types.face_detail.serialize_aws_json_1_1(
                value["face_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FaceRecord:
    out: FaceRecord = {}  # type: ignore[typeddict-item]
    if "Face" in data:
        import aws_sdk_rekognition.types.face

        out["face"] = aws_sdk_rekognition.types.face.deserialize_aws_json_1_1(
            data["Face"]
        )
    if "FaceDetail" in data:
        import aws_sdk_rekognition.types.face_detail

        out["face_detail"] = (
            aws_sdk_rekognition.types.face_detail.deserialize_aws_json_1_1(
                data["FaceDetail"]
            )
        )
    return out
