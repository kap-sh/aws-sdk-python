"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.profile_id


class UpdateProfileResponse(TypedDict, closed=True):
    profile_id: "capo_transfer.types.profile_id.ProfileId"
    """<p>Returns the identifier for the profile that's being updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProfileResponse) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProfileResponse:
    out: UpdateProfileResponse = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("UpdateProfileResponse.profile_id required")
    return out
