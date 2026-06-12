"""Generated from Smithy shape ``com.amazonaws.glue#NotificationProperty``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.notify_delay_after


class NotificationProperty(TypedDict):
    notify_delay_after: NotRequired[
        "aws_sdk_glue.types.notify_delay_after.NotifyDelayAfter"
    ]
    """<p>After a job run starts, the number of minutes to wait before sending a job run delay notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationProperty) -> dict:
    out: dict = {}
    if "notify_delay_after" in value:
        out["NotifyDelayAfter"] = value["notify_delay_after"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationProperty:
    out: NotificationProperty = {}  # type: ignore[typeddict-item]
    if "NotifyDelayAfter" in data:
        out["notify_delay_after"] = data["NotifyDelayAfter"]
    return out
