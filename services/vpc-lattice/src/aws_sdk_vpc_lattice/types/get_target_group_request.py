"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetTargetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.target_group_identifier


class GetTargetGroupRequest(TypedDict, closed=True):
    target_group_identifier: (
        "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier"
    )
    """<p>The ID or ARN of the target group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTargetGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTargetGroupRequest:
    out: GetTargetGroupRequest = {}  # type: ignore[typeddict-item]
    return out
