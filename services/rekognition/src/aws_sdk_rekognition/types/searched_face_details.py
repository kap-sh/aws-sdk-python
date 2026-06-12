"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchedFaceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_detail


class SearchedFaceDetails(TypedDict):
    face_detail: NotRequired["aws_sdk_rekognition.types.face_detail.FaceDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchedFaceDetails) -> dict:
    out: dict = {}
    if "face_detail" in value:
        import aws_sdk_rekognition.types.face_detail

        out["FaceDetail"] = (
            aws_sdk_rekognition.types.face_detail.serialize_aws_json_1_1(
                value["face_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchedFaceDetails:
    out: SearchedFaceDetails = {}  # type: ignore[typeddict-item]
    if "FaceDetail" in data:
        import aws_sdk_rekognition.types.face_detail

        out["face_detail"] = (
            aws_sdk_rekognition.types.face_detail.deserialize_aws_json_1_1(
                data["FaceDetail"]
            )
        )
    return out
