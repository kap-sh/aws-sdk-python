"""Generated from Smithy shape ``com.amazonaws.signer#GetSigningProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.account_id
    import aws_sdk_signer.types.profile_name


class GetSigningProfileRequest(TypedDict):
    profile_name: "aws_sdk_signer.types.profile_name.ProfileName"
    """<p>The name of the target signing profile.</p>"""
    profile_owner: NotRequired["aws_sdk_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the profile owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSigningProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSigningProfileRequest:
    out: GetSigningProfileRequest = {}  # type: ignore[typeddict-item]
    return out
