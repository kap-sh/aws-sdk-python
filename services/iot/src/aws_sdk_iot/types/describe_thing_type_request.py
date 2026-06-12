"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_type_name


class DescribeThingTypeRequest(TypedDict):
    thing_type_name: "aws_sdk_iot.types.thing_type_name.ThingTypeName"
    """<p>The name of the thing type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThingTypeRequest:
    out: DescribeThingTypeRequest = {}  # type: ignore[typeddict-item]
    return out
