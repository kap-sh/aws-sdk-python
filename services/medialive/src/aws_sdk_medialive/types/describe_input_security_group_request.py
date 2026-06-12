"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeInputSecurityGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeInputSecurityGroupRequest(TypedDict):
    input_security_group_id: "aws_sdk_medialive.types.__string.__string"
    """The id of the Input Security Group to describe"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInputSecurityGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInputSecurityGroupRequest:
    out: DescribeInputSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    return out
