"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyPushMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class JourneyPushMessage(TypedDict, closed=True):
    time_to_live: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The number of seconds that the push notification service should keep the message, if the service is unable to deliver the notification the first time. This value is converted to an expiration value when it's sent to a push-notification service. If this value is 0, the service treats the notification as if it expires immediately and the service doesn't store or try to deliver the notification again.</p> <p>This value doesn't apply to messages that are sent through the Amazon Device Messaging (ADM) service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyPushMessage) -> dict:
    out: dict = {}
    if "time_to_live" in value:
        out["TimeToLive"] = value["time_to_live"]
    return out


def deserialize_json(data: dict) -> JourneyPushMessage:
    out: JourneyPushMessage = {}  # type: ignore[typeddict-item]
    if "TimeToLive" in data:
        out["time_to_live"] = data["TimeToLive"]
    return out
