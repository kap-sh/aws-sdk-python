"""Generated from Smithy shape ``com.amazonaws.location#DescribeTrackerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name


class DescribeTrackerRequest(TypedDict):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTrackerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTrackerRequest:
    out: DescribeTrackerRequest = {}  # type: ignore[typeddict-item]
    return out
