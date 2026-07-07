"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.agent_attributes
    import aws_sdk_qconnect.types.custom_attributes
    import aws_sdk_qconnect.types.customer_profile_attributes
    import aws_sdk_qconnect.types.system_attributes


class MessageTemplateAttributes(TypedDict, closed=True):
    system_attributes: NotRequired[
        "aws_sdk_qconnect.types.system_attributes.SystemAttributes"
    ]
    """<p>The system attributes that are used with the message template.</p>"""
    agent_attributes: NotRequired[
        "aws_sdk_qconnect.types.agent_attributes.AgentAttributes"
    ]
    """<p>The agent attributes that are used with the message template.</p>"""
    customer_profile_attributes: NotRequired[
        "aws_sdk_qconnect.types.customer_profile_attributes.CustomerProfileAttributes"
    ]
    """<p>The customer profile attributes that are used with the message template.</p>"""
    custom_attributes: NotRequired[
        "aws_sdk_qconnect.types.custom_attributes.CustomAttributes"
    ]
    """<p>The custom attributes that are used with the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateAttributes) -> dict:
    out: dict = {}
    if "system_attributes" in value:
        import aws_sdk_qconnect.types.system_attributes

        out["systemAttributes"] = (
            aws_sdk_qconnect.types.system_attributes.serialize_json(
                value["system_attributes"]
            )
        )
    if "agent_attributes" in value:
        import aws_sdk_qconnect.types.agent_attributes

        out["agentAttributes"] = aws_sdk_qconnect.types.agent_attributes.serialize_json(
            value["agent_attributes"]
        )
    if "customer_profile_attributes" in value:
        import aws_sdk_qconnect.types.customer_profile_attributes

        out["customerProfileAttributes"] = (
            aws_sdk_qconnect.types.customer_profile_attributes.serialize_json(
                value["customer_profile_attributes"]
            )
        )
    if "custom_attributes" in value:
        import aws_sdk_qconnect.types.custom_attributes

        out["customAttributes"] = (
            aws_sdk_qconnect.types.custom_attributes.serialize_json(
                value["custom_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageTemplateAttributes:
    out: MessageTemplateAttributes = {}  # type: ignore[typeddict-item]
    if "systemAttributes" in data:
        import aws_sdk_qconnect.types.system_attributes

        out["system_attributes"] = (
            aws_sdk_qconnect.types.system_attributes.deserialize_json(
                data["systemAttributes"]
            )
        )
    if "agentAttributes" in data:
        import aws_sdk_qconnect.types.agent_attributes

        out["agent_attributes"] = (
            aws_sdk_qconnect.types.agent_attributes.deserialize_json(
                data["agentAttributes"]
            )
        )
    if "customerProfileAttributes" in data:
        import aws_sdk_qconnect.types.customer_profile_attributes

        out["customer_profile_attributes"] = (
            aws_sdk_qconnect.types.customer_profile_attributes.deserialize_json(
                data["customerProfileAttributes"]
            )
        )
    if "customAttributes" in data:
        import aws_sdk_qconnect.types.custom_attributes

        out["custom_attributes"] = (
            aws_sdk_qconnect.types.custom_attributes.deserialize_json(
                data["customAttributes"]
            )
        )
    return out
