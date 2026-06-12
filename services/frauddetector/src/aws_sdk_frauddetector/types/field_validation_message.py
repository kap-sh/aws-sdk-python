"""Generated from Smithy shape ``com.amazonaws.frauddetector#FieldValidationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string


class FieldValidationMessage(TypedDict):
    field_name: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The field name.</p>"""
    identifier: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The message ID.</p>"""
    title: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The message title.</p>"""
    content: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The message content.</p>"""
    type: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The message type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldValidationMessage) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["fieldName"] = value["field_name"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "title" in value:
        out["title"] = value["title"]
    if "content" in value:
        out["content"] = value["content"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldValidationMessage:
    out: FieldValidationMessage = {}  # type: ignore[typeddict-item]
    if "fieldName" in data:
        out["field_name"] = data["fieldName"]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    if "title" in data:
        out["title"] = data["title"]
    if "content" in data:
        out["content"] = data["content"]
    if "type" in data:
        out["type"] = data["type"]
    return out
