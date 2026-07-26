"""Generated from Smithy shape ``com.amazonaws.location#DescribeMapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.resource_name


class DescribeMapRequest(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the map resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMapRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeMapRequest:
    out: DescribeMapRequest = {}  # type: ignore[typeddict-item]
    return out
