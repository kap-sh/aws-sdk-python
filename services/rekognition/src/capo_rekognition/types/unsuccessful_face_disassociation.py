"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDisassociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.face_id
    import capo_rekognition.types.unsuccessful_face_disassociation_reasons
    import capo_rekognition.types.user_id


class UnsuccessfulFaceDisassociation(TypedDict, closed=True):
    face_id: NotRequired["capo_rekognition.types.face_id.FaceId"]
    """<p>A unique identifier assigned to the face. </p>"""
    user_id: NotRequired["capo_rekognition.types.user_id.UserId"]
    """<p>A provided ID for the UserID. Unique within the collection. </p>"""
    reasons: NotRequired[
        "capo_rekognition.types.unsuccessful_face_disassociation_reasons.UnsuccessfulFaceDisassociationReasons"
    ]
    """<p>The reason why the deletion was unsuccessful. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceDisassociation) -> dict:
    out: dict = {}
    if "face_id" in value:
        out["FaceId"] = value["face_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "reasons" in value:
        import capo_rekognition.types.unsuccessful_face_disassociation_reasons

        out["Reasons"] = (
            capo_rekognition.types.unsuccessful_face_disassociation_reasons.serialize_aws_json_1_1(
                value["reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsuccessfulFaceDisassociation:
    out: UnsuccessfulFaceDisassociation = {}  # type: ignore[typeddict-item]
    if "FaceId" in data:
        out["face_id"] = data["FaceId"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "Reasons" in data:
        import capo_rekognition.types.unsuccessful_face_disassociation_reasons

        out["reasons"] = (
            capo_rekognition.types.unsuccessful_face_disassociation_reasons.deserialize_aws_json_1_1(
                data["Reasons"]
            )
        )
    return out
