"""Generated from Smithy shape ``com.amazonaws.iot#AttachSecurityProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.security_profile_name
    import aws_sdk_iot.types.security_profile_target_arn


class AttachSecurityProfileRequest(TypedDict):
    security_profile_name: "aws_sdk_iot.types.security_profile_name.SecurityProfileName"
    """<p>The security profile that is attached.</p>"""
    security_profile_target_arn: (
        "aws_sdk_iot.types.security_profile_target_arn.SecurityProfileTargetArn"
    )
    """<p>The ARN of the target (thing group) to which the security profile is attached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachSecurityProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AttachSecurityProfileRequest:
    out: AttachSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    return out
