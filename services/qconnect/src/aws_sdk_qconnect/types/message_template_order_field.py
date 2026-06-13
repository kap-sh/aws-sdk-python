"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateOrderField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.order


class MessageTemplateOrderField(TypedDict):
    name: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the message template.</p>"""
    order: NotRequired["aws_sdk_qconnect.types.order.Order"]
    """<p>The order at which the message templates are sorted by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateOrderField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "order" in value:
        out["order"] = value["order"]
    return out


def deserialize_json(data: dict) -> MessageTemplateOrderField:
    out: MessageTemplateOrderField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MessageTemplateOrderField.name required")
    if "order" in data:
        out["order"] = data["order"]
    return out
