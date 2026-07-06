"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.message_header_name
    import aws_sdk_sesv2.types.message_header_value


class MessageHeader(TypedDict, closed=True):
    name: "aws_sdk_sesv2.types.message_header_name.MessageHeaderName"
    """<p>The name of the message header. The message header name has to meet the following criteria:</p> <ul> <li> <p>Can contain any printable ASCII character (33 - 126) except for colon (:).</p> </li> <li> <p>Can contain no more than 126 characters.</p> </li> </ul>"""
    value: "aws_sdk_sesv2.types.message_header_value.MessageHeaderValue"
    """<p>The value of the message header. The message header value has to meet the following criteria:</p> <ul> <li> <p>Can contain any printable ASCII character.</p> </li> <li> <p>Can contain no more than 995 characters.</p> </li> <li> <p>The combined length of the header name and value must not exceed 996 characters.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageHeader) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> MessageHeader:
    out: MessageHeader = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("MessageHeader.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("MessageHeader.value required")
    return out
