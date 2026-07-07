"""Generated from Smithy shape ``com.amazonaws.qconnect#SystemAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_attribute_value
    import aws_sdk_qconnect.types.system_endpoint_attributes


class SystemAttributes(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The name of the task.</p>"""
    customer_endpoint: NotRequired[
        "aws_sdk_qconnect.types.system_endpoint_attributes.SystemEndpointAttributes"
    ]
    """<p>The CustomerEndpoint attribute.</p>"""
    system_endpoint: NotRequired[
        "aws_sdk_qconnect.types.system_endpoint_attributes.SystemEndpointAttributes"
    ]
    """<p>The SystemEndpoint attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemAttributes) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "customer_endpoint" in value:
        import aws_sdk_qconnect.types.system_endpoint_attributes

        out["customerEndpoint"] = (
            aws_sdk_qconnect.types.system_endpoint_attributes.serialize_json(
                value["customer_endpoint"]
            )
        )
    if "system_endpoint" in value:
        import aws_sdk_qconnect.types.system_endpoint_attributes

        out["systemEndpoint"] = (
            aws_sdk_qconnect.types.system_endpoint_attributes.serialize_json(
                value["system_endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemAttributes:
    out: SystemAttributes = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "customerEndpoint" in data:
        import aws_sdk_qconnect.types.system_endpoint_attributes

        out["customer_endpoint"] = (
            aws_sdk_qconnect.types.system_endpoint_attributes.deserialize_json(
                data["customerEndpoint"]
            )
        )
    if "systemEndpoint" in data:
        import aws_sdk_qconnect.types.system_endpoint_attributes

        out["system_endpoint"] = (
            aws_sdk_qconnect.types.system_endpoint_attributes.deserialize_json(
                data["systemEndpoint"]
            )
        )
    return out
