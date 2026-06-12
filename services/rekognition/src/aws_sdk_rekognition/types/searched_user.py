"""Generated from Smithy shape ``com.amazonaws.rekognition#SearchedUser``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.user_id


class SearchedUser(TypedDict):
    user_id: NotRequired["aws_sdk_rekognition.types.user_id.UserId"]
    """<p> A provided ID for the UserID. Unique within the collection. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchedUser) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchedUser:
    out: SearchedUser = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    return out
