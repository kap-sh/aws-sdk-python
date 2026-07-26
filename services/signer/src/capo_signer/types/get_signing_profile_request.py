"""Generated from Smithy shape ``com.amazonaws.signer#GetSigningProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.account_id
    import capo_signer.types.profile_name


class GetSigningProfileRequest(TypedDict, closed=True):
    profile_name: "capo_signer.types.profile_name.ProfileName"
    """<p>The name of the target signing profile.</p>"""
    profile_owner: NotRequired["capo_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the profile owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSigningProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSigningProfileRequest:
    out: GetSigningProfileRequest = {}  # type: ignore[typeddict-item]
    return out
