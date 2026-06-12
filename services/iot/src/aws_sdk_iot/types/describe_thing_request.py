"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_name


class DescribeThingRequest(TypedDict):
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThingRequest:
    out: DescribeThingRequest = {}  # type: ignore[typeddict-item]
    return out
