"""Generated from Smithy shape ``com.amazonaws.outposts#CancelCapacityTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.capacity_task_id
    import aws_sdk_outposts.types.outpost_identifier


class CancelCapacityTaskInput(TypedDict):
    capacity_task_id: "aws_sdk_outposts.types.capacity_task_id.CapacityTaskId"
    """<p>ID of the capacity task that you want to cancel.</p>"""
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>ID or ARN of the Outpost associated with the capacity task that you want to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelCapacityTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelCapacityTaskInput:
    out: CancelCapacityTaskInput = {}  # type: ignore[typeddict-item]
    return out
