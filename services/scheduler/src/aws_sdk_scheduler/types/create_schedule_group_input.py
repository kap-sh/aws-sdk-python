"""Generated from Smithy shape ``com.amazonaws.scheduler#CreateScheduleGroupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.client_token
    import aws_sdk_scheduler.types.schedule_group_name
    import aws_sdk_scheduler.types.tag_list


class CreateScheduleGroupInput(TypedDict):
    name: "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName"
    """<p>The name of the schedule group that you are creating.</p>"""
    tags: NotRequired["aws_sdk_scheduler.types.tag_list.TagList"]
    """<p>The list of tags to associate with the schedule group.</p>"""
    client_token: NotRequired["aws_sdk_scheduler.types.client_token.ClientToken"]
    """<p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleGroupInput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_scheduler.types.tag_list

        out["Tags"] = aws_sdk_scheduler.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateScheduleGroupInput:
    out: CreateScheduleGroupInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_scheduler.types.tag_list

        out["tags"] = aws_sdk_scheduler.types.tag_list.deserialize_json(data["Tags"])
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
