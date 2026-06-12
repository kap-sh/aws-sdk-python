"""Generated from Smithy shape ``com.amazonaws.amplifybackend#EmailSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class EmailSettings(TypedDict):
    email_message: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The contents of the email message.</p>"""
    email_subject: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The contents of the subject line of the email message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailSettings) -> dict:
    out: dict = {}
    if "email_message" in value:
        out["emailMessage"] = value["email_message"]
    if "email_subject" in value:
        out["emailSubject"] = value["email_subject"]
    return out


def deserialize_json(data: dict) -> EmailSettings:
    out: EmailSettings = {}  # type: ignore[typeddict-item]
    if "emailMessage" in data:
        out["email_message"] = data["emailMessage"]
    if "emailSubject" in data:
        out["email_subject"] = data["emailSubject"]
    return out
