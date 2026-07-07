"""Generated from Smithy shape ``com.amazonaws.workdocs#NotificationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.boolean_type
    import aws_sdk_workdocs.types.message_type


class NotificationOptions(TypedDict, closed=True):
    send_email: "aws_sdk_workdocs.types.boolean_type.BooleanType"
    """<p>Boolean value to indicate an email notification should be sent to the recipients.</p>"""
    email_message: NotRequired["aws_sdk_workdocs.types.message_type.MessageType"]
    """<p>Text value to be included in the email body.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationOptions) -> dict:
    out: dict = {}
    out["SendEmail"] = value.get("send_email", False)
    if "email_message" in value:
        out["EmailMessage"] = value["email_message"]
    return out


def deserialize_json(data: dict) -> NotificationOptions:
    out: NotificationOptions = {}  # type: ignore[typeddict-item]
    if "SendEmail" in data:
        out["send_email"] = data["SendEmail"]
    else:
        out["send_email"] = False
    if "EmailMessage" in data:
        out["email_message"] = data["EmailMessage"]
    return out
