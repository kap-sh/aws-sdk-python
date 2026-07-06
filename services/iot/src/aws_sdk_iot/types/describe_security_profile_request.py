"""Generated from Smithy shape ``com.amazonaws.iot#DescribeSecurityProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.security_profile_name


class DescribeSecurityProfileRequest(TypedDict, closed=True):
    security_profile_name: "aws_sdk_iot.types.security_profile_name.SecurityProfileName"
    """<p>The name of the security profile whose information you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSecurityProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSecurityProfileRequest:
    out: DescribeSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    return out
