"""Generated from Smithy shape ``com.amazonaws.rekognition#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.user_id
    import capo_rekognition.types.user_status


class User(TypedDict, closed=True):
    user_id: NotRequired["capo_rekognition.types.user_id.UserId"]
    """<p> A provided ID for the User. Unique within the collection.</p>"""
    user_status: NotRequired["capo_rekognition.types.user_status.UserStatus"]
    """<p> Communicates if the UserID has been updated with latest set of faces to be associated with the UserID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: User) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "user_status" in value:
        import capo_rekognition.types.user_status

        out["UserStatus"] = capo_rekognition.types.user_status.serialize_aws_json_1_1(
            value["user_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "UserStatus" in data:
        import capo_rekognition.types.user_status

        out["user_status"] = (
            capo_rekognition.types.user_status.deserialize_aws_json_1_1(
                data["UserStatus"]
            )
        )
    return out
