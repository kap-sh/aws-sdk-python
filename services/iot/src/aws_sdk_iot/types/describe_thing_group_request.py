"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_group_name


class DescribeThingGroupRequest(TypedDict, closed=True):
    thing_group_name: "aws_sdk_iot.types.thing_group_name.ThingGroupName"
    """<p>The name of the thing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThingGroupRequest:
    out: DescribeThingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
