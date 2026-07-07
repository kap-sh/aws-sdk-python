"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxScalingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_environment_id
    import aws_sdk_finspace.types.kx_scaling_group_name


class GetKxScalingGroupRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment. </p>"""
    scaling_group_name: (
        "aws_sdk_finspace.types.kx_scaling_group_name.KxScalingGroupName"
    )
    """<p>A unique identifier for the kdb scaling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxScalingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxScalingGroupRequest:
    out: GetKxScalingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
