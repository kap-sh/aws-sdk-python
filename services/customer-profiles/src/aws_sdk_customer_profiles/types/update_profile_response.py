"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.uuid


class UpdateProfileResponse(TypedDict, closed=True):
    profile_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileResponse) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_json(data: dict) -> UpdateProfileResponse:
    out: UpdateProfileResponse = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("UpdateProfileResponse.profile_id required")
    return out
