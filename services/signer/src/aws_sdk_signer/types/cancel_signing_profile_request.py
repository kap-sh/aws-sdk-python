"""Generated from Smithy shape ``com.amazonaws.signer#CancelSigningProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.profile_name


class CancelSigningProfileRequest(TypedDict, closed=True):
    profile_name: "aws_sdk_signer.types.profile_name.ProfileName"
    """<p>The name of the signing profile to be canceled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelSigningProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelSigningProfileRequest:
    out: CancelSigningProfileRequest = {}  # type: ignore[typeddict-item]
    return out
