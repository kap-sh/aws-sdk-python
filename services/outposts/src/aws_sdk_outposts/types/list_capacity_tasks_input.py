"""Generated from Smithy shape ``com.amazonaws.outposts#ListCapacityTasksInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.capacity_task_status_list
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.token


class ListCapacityTasksInput(TypedDict):
    outpost_identifier_filter: NotRequired[
        "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    ]
    """<p>Filters the results by an Outpost ID or an Outpost ARN.</p>"""
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    capacity_task_status_filter: NotRequired[
        "aws_sdk_outposts.types.capacity_task_status_list.CapacityTaskStatusList"
    ]
    """<p>A list of statuses. For example, <code>REQUESTED</code> or <code>WAITING_FOR_EVACUATION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCapacityTasksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCapacityTasksInput:
    out: ListCapacityTasksInput = {}  # type: ignore[typeddict-item]
    return out
