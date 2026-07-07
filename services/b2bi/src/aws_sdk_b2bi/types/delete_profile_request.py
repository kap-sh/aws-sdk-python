"""Generated from Smithy shape ``com.amazonaws.b2bi#DeleteProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.profile_id


class DeleteProfileRequest(TypedDict, closed=True):
    profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId"
    """<p>Specifies the unique, system-generated identifier for the profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProfileRequest:
    out: DeleteProfileRequest = {}  # type: ignore[typeddict-item]
    return out
