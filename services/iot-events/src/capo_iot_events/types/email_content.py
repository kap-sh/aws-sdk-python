"""Generated from Smithy shape ``com.amazonaws.iotevents#EmailContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.email_subject
    import capo_iot_events.types.notification_additional_message


class EmailContent(TypedDict, closed=True):
    subject: NotRequired["capo_iot_events.types.email_subject.EmailSubject"]
    """<p>The subject of the email.</p>"""
    additional_message: NotRequired[
        "capo_iot_events.types.notification_additional_message.NotificationAdditionalMessage"
    ]
    """<p>The message that you want to send. The message can be up to 200 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailContent) -> dict:
    out: dict = {}
    if "subject" in value:
        out["subject"] = value["subject"]
    if "additional_message" in value:
        out["additionalMessage"] = value["additional_message"]
    return out


def deserialize_json(data: dict) -> EmailContent:
    out: EmailContent = {}  # type: ignore[typeddict-item]
    if "subject" in data:
        out["subject"] = data["subject"]
    if "additionalMessage" in data:
        out["additional_message"] = data["additionalMessage"]
    return out
