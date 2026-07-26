"""Generated from Smithy shape ``com.amazonaws.outposts#ListCapacityTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.capacity_task_status_list
    import capo_outposts.types.max_results1000
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.token


class ListCapacityTasksInput(TypedDict, closed=True):
    outpost_identifier_filter: NotRequired[
        "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    ]
    """<p>Filters the results by an Outpost ID or an Outpost ARN.</p>"""
    max_results: NotRequired["capo_outposts.types.max_results1000.MaxResults1000"]
    next_token: NotRequired["capo_outposts.types.token.Token"]
    capacity_task_status_filter: NotRequired[
        "capo_outposts.types.capacity_task_status_list.CapacityTaskStatusList"
    ]
    """<p>A list of statuses. For example, <code>REQUESTED</code> or <code>WAITING_FOR_EVACUATION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCapacityTasksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCapacityTasksInput:
    out: ListCapacityTasksInput = {}  # type: ignore[typeddict-item]
    return out
