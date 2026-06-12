"""Generated from Smithy shape ``com.amazonaws.b2bi#GetProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.profile_id


class GetProfileRequest(TypedDict):
    profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId"
    """<p>Specifies the unique, system-generated identifier for the profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProfileRequest:
    out: GetProfileRequest = {}  # type: ignore[typeddict-item]
    return out
