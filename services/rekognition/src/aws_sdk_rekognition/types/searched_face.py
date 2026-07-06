"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchedFace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_id


class SearchedFace(TypedDict, closed=True):
    face_id: NotRequired["aws_sdk_rekognition.types.face_id.FaceId"]
    """<p> Unique identifier assigned to the face.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchedFace) -> dict:
    out: dict = {}
    if "face_id" in value:
        out["FaceId"] = value["face_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchedFace:
    out: SearchedFace = {}  # type: ignore[typeddict-item]
    if "FaceId" in data:
        out["face_id"] = data["FaceId"]
    return out
