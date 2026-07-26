"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchedFaceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.face_detail


class SearchedFaceDetails(TypedDict, closed=True):
    face_detail: NotRequired["capo_rekognition.types.face_detail.FaceDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchedFaceDetails) -> dict:
    out: dict = {}
    if "face_detail" in value:
        import capo_rekognition.types.face_detail

        out["FaceDetail"] = capo_rekognition.types.face_detail.serialize_aws_json_1_1(
            value["face_detail"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchedFaceDetails:
    out: SearchedFaceDetails = {}  # type: ignore[typeddict-item]
    if "FaceDetail" in data:
        import capo_rekognition.types.face_detail

        out["face_detail"] = (
            capo_rekognition.types.face_detail.deserialize_aws_json_1_1(
                data["FaceDetail"]
            )
        )
    return out
