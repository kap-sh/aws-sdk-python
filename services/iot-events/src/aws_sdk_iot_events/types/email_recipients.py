"""Generated from Smithy shape ``com.amazonaws.iotevents#EmailRecipients``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.recipient_details


class EmailRecipients(TypedDict):
    to: NotRequired["aws_sdk_iot_events.types.recipient_details.RecipientDetails"]
    """<p>Specifies one or more recipients who receive the email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailRecipients) -> dict:
    out: dict = {}
    if "to" in value:
        import aws_sdk_iot_events.types.recipient_details

        out["to"] = aws_sdk_iot_events.types.recipient_details.serialize_json(
            value["to"]
        )
    return out


def deserialize_json(data: dict) -> EmailRecipients:
    out: EmailRecipients = {}  # type: ignore[typeddict-item]
    if "to" in data:
        import aws_sdk_iot_events.types.recipient_details

        out["to"] = aws_sdk_iot_events.types.recipient_details.deserialize_json(
            data["to"]
        )
    return out
