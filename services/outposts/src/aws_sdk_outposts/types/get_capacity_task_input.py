"""Generated from Smithy shape ``com.amazonaws.outposts#GetCapacityTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.capacity_task_id
    import aws_sdk_outposts.types.outpost_identifier


class GetCapacityTaskInput(TypedDict, closed=True):
    capacity_task_id: "aws_sdk_outposts.types.capacity_task_id.CapacityTaskId"
    """<p>ID of the capacity task.</p>"""
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>ID or ARN of the Outpost associated with the specified capacity task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCapacityTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCapacityTaskInput:
    out: GetCapacityTaskInput = {}  # type: ignore[typeddict-item]
    return out
