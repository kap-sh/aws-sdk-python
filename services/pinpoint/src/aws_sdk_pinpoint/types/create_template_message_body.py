"""Generated from Smithy shape ``com.amazonaws.pinpoint#CreateTemplateMessageBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class CreateTemplateMessageBody(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the message template that was created.</p>"""
    message: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message that's returned from the API for the request to create the message template.</p>"""
    request_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the request to create the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateMessageBody) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestID"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateTemplateMessageBody:
    out: CreateTemplateMessageBody = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestID" in data:
        out["request_id"] = data["RequestID"]
    return out
