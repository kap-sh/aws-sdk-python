"""Generated from Smithy shape ``com.amazonaws.frauddetector#FileValidationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string


class FileValidationMessage(TypedDict):
    title: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The message title.</p>"""
    content: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The message content.</p>"""
    type: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The message type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileValidationMessage) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "content" in value:
        out["content"] = value["content"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileValidationMessage:
    out: FileValidationMessage = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "content" in data:
        out["content"] = data["content"]
    if "type" in data:
        out["type"] = data["type"]
    return out
