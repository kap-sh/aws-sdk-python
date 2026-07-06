"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_id
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.unsuccessful_face_association_reasons
    import aws_sdk_rekognition.types.user_id


class UnsuccessfulFaceAssociation(TypedDict, closed=True):
    face_id: NotRequired["aws_sdk_rekognition.types.face_id.FaceId"]
    """<p>A unique identifier assigned to the face. </p>"""
    user_id: NotRequired["aws_sdk_rekognition.types.user_id.UserId"]
    """<p>A provided ID for the UserID. Unique within the collection. </p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Match confidence with the UserID, provides information regarding if a face association was unsuccessful because it didn't meet UserMatchThreshold.</p>"""
    reasons: NotRequired[
        "aws_sdk_rekognition.types.unsuccessful_face_association_reasons.UnsuccessfulFaceAssociationReasons"
    ]
    """<p> The reason why the association was unsuccessful. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceAssociation) -> dict:
    out: dict = {}
    if "face_id" in value:
        out["FaceId"] = value["face_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "reasons" in value:
        import aws_sdk_rekognition.types.unsuccessful_face_association_reasons

        out["Reasons"] = (
            aws_sdk_rekognition.types.unsuccessful_face_association_reasons.serialize_aws_json_1_1(
                value["reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsuccessfulFaceAssociation:
    out: UnsuccessfulFaceAssociation = {}  # type: ignore[typeddict-item]
    if "FaceId" in data:
        out["face_id"] = data["FaceId"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Reasons" in data:
        import aws_sdk_rekognition.types.unsuccessful_face_association_reasons

        out["reasons"] = (
            aws_sdk_rekognition.types.unsuccessful_face_association_reasons.deserialize_aws_json_1_1(
                data["Reasons"]
            )
        )
    return out
