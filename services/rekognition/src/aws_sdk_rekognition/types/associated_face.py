"""Generated from Smithy shape ``com.amazonaws.rekognition#AssociatedFace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_id


class AssociatedFace(TypedDict):
    face_id: NotRequired["aws_sdk_rekognition.types.face_id.FaceId"]
    """<p>Unique identifier assigned to the face.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedFace) -> dict:
    out: dict = {}
    if "face_id" in value:
        out["FaceId"] = value["face_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatedFace:
    out: AssociatedFace = {}  # type: ignore[typeddict-item]
    if "FaceId" in data:
        out["face_id"] = data["FaceId"]
    return out
