"""Generated from Smithy shape ``com.amazonaws.outposts#CancelCapacityTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.capacity_task_id
    import capo_outposts.types.outpost_identifier


class CancelCapacityTaskInput(TypedDict, closed=True):
    capacity_task_id: "capo_outposts.types.capacity_task_id.CapacityTaskId"
    """<p>ID of the capacity task that you want to cancel.</p>"""
    outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>ID or ARN of the Outpost associated with the capacity task that you want to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelCapacityTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelCapacityTaskInput:
    out: CancelCapacityTaskInput = {}  # type: ignore[typeddict-item]
    return out
