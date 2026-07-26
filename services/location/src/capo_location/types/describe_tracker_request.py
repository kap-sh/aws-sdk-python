"""Generated from Smithy shape ``com.amazonaws.location#DescribeTrackerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.resource_name


class DescribeTrackerRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTrackerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTrackerRequest:
    out: DescribeTrackerRequest = {}  # type: ignore[typeddict-item]
    return out
