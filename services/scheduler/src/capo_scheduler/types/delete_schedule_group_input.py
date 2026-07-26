"""Generated from Smithy shape ``com.amazonaws.scheduler#DeleteScheduleGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.client_token
    import capo_scheduler.types.schedule_group_name


class DeleteScheduleGroupInput(TypedDict, closed=True):
    name: "capo_scheduler.types.schedule_group_name.ScheduleGroupName"
    """<p>The name of the schedule group to delete.</p>"""
    client_token: NotRequired["capo_scheduler.types.client_token.ClientToken"]
    """<p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleGroupInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScheduleGroupInput:
    out: DeleteScheduleGroupInput = {}  # type: ignore[typeddict-item]
    return out
