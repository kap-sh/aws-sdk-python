"""Generated from Smithy shape ``com.amazonaws.scheduler#DeleteScheduleInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.client_token
    import aws_sdk_scheduler.types.name
    import aws_sdk_scheduler.types.schedule_group_name


class DeleteScheduleInput(TypedDict):
    name: "aws_sdk_scheduler.types.name.Name"
    """<p>The name of the schedule to delete.</p>"""
    group_name: NotRequired[
        "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName"
    ]
    """<p>The name of the schedule group associated with this schedule. If you omit this, the default schedule group is used.</p>"""
    client_token: NotRequired["aws_sdk_scheduler.types.client_token.ClientToken"]
    """<p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScheduleInput:
    out: DeleteScheduleInput = {}  # type: ignore[typeddict-item]
    return out
