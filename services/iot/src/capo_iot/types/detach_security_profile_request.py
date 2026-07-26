"""Generated from Smithy shape ``com.amazonaws.iot#DetachSecurityProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.security_profile_name
    import capo_iot.types.security_profile_target_arn


class DetachSecurityProfileRequest(TypedDict, closed=True):
    security_profile_name: "capo_iot.types.security_profile_name.SecurityProfileName"
    """<p>The security profile that is detached.</p>"""
    security_profile_target_arn: (
        "capo_iot.types.security_profile_target_arn.SecurityProfileTargetArn"
    )
    """<p>The ARN of the thing group from which the security profile is detached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachSecurityProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DetachSecurityProfileRequest:
    out: DetachSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    return out
