"""Generated from Smithy shape ``com.amazonaws.qconnect#AgentAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_attribute_value


class AgentAttributes(TypedDict):
    first_name: NotRequired[
        "aws_sdk_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The agent’s first name as entered in their Amazon Connect user account.</p>"""
    last_name: NotRequired[
        "aws_sdk_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The agent’s last name as entered in their Amazon Connect user account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentAttributes) -> dict:
    out: dict = {}
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    return out


def deserialize_json(data: dict) -> AgentAttributes:
    out: AgentAttributes = {}  # type: ignore[typeddict-item]
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    return out
