"""Generated from Smithy shape ``com.amazonaws.connect#CreateSecurityProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.security_profile_id


class CreateSecurityProfileResponse(TypedDict, closed=True):
    security_profile_id: NotRequired[
        "capo_connect.types.security_profile_id.SecurityProfileId"
    ]
    """<p>The identifier for the security profle.</p>"""
    security_profile_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the security profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityProfileResponse) -> dict:
    out: dict = {}
    if "security_profile_id" in value:
        out["SecurityProfileId"] = value["security_profile_id"]
    if "security_profile_arn" in value:
        out["SecurityProfileArn"] = value["security_profile_arn"]
    return out


def deserialize_json(data: dict) -> CreateSecurityProfileResponse:
    out: CreateSecurityProfileResponse = {}  # type: ignore[typeddict-item]
    if "SecurityProfileId" in data:
        out["security_profile_id"] = data["SecurityProfileId"]
    if "SecurityProfileArn" in data:
        out["security_profile_arn"] = data["SecurityProfileArn"]
    return out
