"""Generated from Smithy shape ``com.amazonaws.scheduler#CreateScheduleGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.client_token
    import capo_scheduler.types.schedule_group_name
    import capo_scheduler.types.tag_list


class CreateScheduleGroupInput(TypedDict, closed=True):
    name: "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
    """<p>The name of the schedule group that you are creating.</p>"""
    tags: NotRequired["capo_scheduler.types.tag_list.TagList"]
    """<p>The list of tags to associate with the schedule group.</p>"""
    client_token: NotRequired["capo_scheduler.types.client_token.ClientToken"]
    """<p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleGroupInput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_scheduler.types.tag_list

        out["Tags"] = capo_scheduler.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateScheduleGroupInput:
    out: CreateScheduleGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_scheduler.types.tag_list

        out["tags"] = capo_scheduler.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
