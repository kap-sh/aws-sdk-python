"""Generated from Smithy shape ``com.amazonaws.ses#MessageTag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.message_tag_name
    import aws_sdk_ses.types.message_tag_value


class MessageTag(TypedDict):
    name: "aws_sdk_ses.types.message_tag_name.MessageTagName"
    """<p>The name of the tag. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Contain 256 characters or fewer.</p> </li> </ul>"""
    value: "aws_sdk_ses.types.message_tag_value.MessageTagValue"
    """<p>The value of the tag. The value must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Contain 256 characters or fewer.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MessageTag, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Name", str(value["name"])))
    pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> MessageTag:
    out: MessageTag = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("MessageTag.name required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        raise DeserializationError("MessageTag.value required")
    return out
