"""Generated from Smithy shape ``com.amazonaws.scheduler#ListScheduleGroupsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.max_results
    import aws_sdk_scheduler.types.next_token
    import aws_sdk_scheduler.types.schedule_group_name_prefix


class ListScheduleGroupsInput(TypedDict):
    name_prefix: NotRequired[
        "aws_sdk_scheduler.types.schedule_group_name_prefix.ScheduleGroupNamePrefix"
    ]
    """<p>The name prefix that you can use to return a filtered list of your schedule groups.</p>"""
    next_token: NotRequired["aws_sdk_scheduler.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_scheduler.types.max_results.MaxResults"]
    """<p>If specified, limits the number of results returned by this operation. The operation also returns a <code>NextToken</code> which you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScheduleGroupsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListScheduleGroupsInput:
    out: ListScheduleGroupsInput = {}  # type: ignore[typeddict-item]
    return out
