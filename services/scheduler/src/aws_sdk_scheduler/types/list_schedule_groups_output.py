"""Generated from Smithy shape ``com.amazonaws.scheduler#ListScheduleGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.next_token
    import aws_sdk_scheduler.types.schedule_group_list


class ListScheduleGroupsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_scheduler.types.next_token.NextToken"]
    """<p>Indicates whether there are additional results to retrieve. If the value is null, there are no more results.</p>"""
    schedule_groups: "aws_sdk_scheduler.types.schedule_group_list.ScheduleGroupList"
    """<p>The schedule groups that match the specified criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScheduleGroupsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_scheduler.types.schedule_group_list

    out["ScheduleGroups"] = aws_sdk_scheduler.types.schedule_group_list.serialize_json(
        value["schedule_groups"]
    )
    return out


def deserialize_json(data: dict) -> ListScheduleGroupsOutput:
    out: ListScheduleGroupsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ScheduleGroups" in data:
        import aws_sdk_scheduler.types.schedule_group_list

        out["schedule_groups"] = (
            aws_sdk_scheduler.types.schedule_group_list.deserialize_json(
                data["ScheduleGroups"]
            )
        )
    else:
        raise DeserializationError("ListScheduleGroupsOutput.schedule_groups required")
    return out
