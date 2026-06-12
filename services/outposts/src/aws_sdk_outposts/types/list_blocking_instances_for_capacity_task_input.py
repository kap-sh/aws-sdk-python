"""Generated from Smithy shape ``com.amazonaws.outposts#ListBlockingInstancesForCapacityTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.capacity_task_id
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.token


class ListBlockingInstancesForCapacityTaskInput(TypedDict):
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost associated with the specified capacity task.</p>"""
    capacity_task_id: "aws_sdk_outposts.types.capacity_task_id.CapacityTaskId"
    """<p>The ID of the capacity task.</p>"""
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListBlockingInstancesForCapacityTaskInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBlockingInstancesForCapacityTaskInput:
    out: ListBlockingInstancesForCapacityTaskInput = {}  # type: ignore[typeddict-item]
    return out
