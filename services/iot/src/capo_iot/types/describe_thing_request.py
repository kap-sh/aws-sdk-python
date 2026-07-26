"""Generated from Smithy shape ``com.amazonaws.iot#DescribeThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.thing_name


class DescribeThingRequest(TypedDict, closed=True):
    thing_name: "capo_iot.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThingRequest:
    out: DescribeThingRequest = {}  # type: ignore[typeddict-item]
    return out
