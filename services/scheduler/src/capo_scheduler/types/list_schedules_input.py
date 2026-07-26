"""Generated from Smithy shape ``com.amazonaws.scheduler#ListSchedulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.max_results
    import capo_scheduler.types.name_prefix
    import capo_scheduler.types.next_token
    import capo_scheduler.types.schedule_group_name
    import capo_scheduler.types.schedule_state


class ListSchedulesInput(TypedDict, closed=True):
    group_name: NotRequired[
        "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
    ]
    """<p>If specified, only lists the schedules whose associated schedule group matches the given filter.</p>"""
    name_prefix: NotRequired["capo_scheduler.types.name_prefix.NamePrefix"]
    """<p>Schedule name prefix to return the filtered list of resources.</p>"""
    state: NotRequired["capo_scheduler.types.schedule_state.ScheduleState"]
    """<p>If specified, only lists the schedules whose current state matches the given filter.</p>"""
    next_token: NotRequired["capo_scheduler.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_scheduler.types.max_results.MaxResults"]
    """<p>If specified, limits the number of results returned by this operation. The operation also returns a <code>NextToken</code> which you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchedulesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSchedulesInput:
    out: ListSchedulesInput = {}  # type: ignore[typeddict-item]
    return out
