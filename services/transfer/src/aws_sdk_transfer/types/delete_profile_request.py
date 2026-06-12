"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.profile_id


class DeleteProfileRequest(TypedDict):
    profile_id: "aws_sdk_transfer.types.profile_id.ProfileId"
    """<p>The identifier of the profile that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProfileRequest:
    out: DeleteProfileRequest = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("DeleteProfileRequest.profile_id required")
    return out
