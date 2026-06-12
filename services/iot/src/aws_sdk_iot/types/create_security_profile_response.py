"""Generated from Smithy shape ``com.amazonaws.iot#CreateSecurityProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.security_profile_arn
    import aws_sdk_iot.types.security_profile_name


class CreateSecurityProfileResponse(TypedDict):
    security_profile_name: NotRequired[
        "aws_sdk_iot.types.security_profile_name.SecurityProfileName"
    ]
    """<p>The name you gave to the security profile.</p>"""
    security_profile_arn: NotRequired[
        "aws_sdk_iot.types.security_profile_arn.SecurityProfileArn"
    ]
    """<p>The ARN of the security profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityProfileResponse) -> dict:
    out: dict = {}
    if "security_profile_name" in value:
        out["securityProfileName"] = value["security_profile_name"]
    if "security_profile_arn" in value:
        out["securityProfileArn"] = value["security_profile_arn"]
    return out


def deserialize_json(data: dict) -> CreateSecurityProfileResponse:
    out: CreateSecurityProfileResponse = {}  # type: ignore[typeddict-item]
    if "securityProfileName" in data:
        out["security_profile_name"] = data["securityProfileName"]
    if "securityProfileArn" in data:
        out["security_profile_arn"] = data["securityProfileArn"]
    return out
