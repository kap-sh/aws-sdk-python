"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageTag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.message_tag_name
    import aws_sdk_sesv2.types.message_tag_value


class MessageTag(TypedDict):
    name: "aws_sdk_sesv2.types.message_tag_name.MessageTagName"
    """<p>The name of the message tag. The message tag name has to meet the following criteria:</p> <ul> <li> <p>It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).</p> </li> <li> <p>It can contain no more than 256 characters.</p> </li> </ul>"""
    value: "aws_sdk_sesv2.types.message_tag_value.MessageTagValue"
    """<p>The value of the message tag. The message tag value has to meet the following criteria:</p> <ul> <li> <p>It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).</p> </li> <li> <p>It can contain no more than 256 characters.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTag) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> MessageTag:
    out: MessageTag = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("MessageTag.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("MessageTag.value required")
    return out
