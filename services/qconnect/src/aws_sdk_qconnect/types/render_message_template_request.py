"""Generated from Smithy shape ``com.amazonaws.qconnect#RenderMessageTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_attributes
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier


class RenderMessageTemplateRequest(TypedDict):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN.</p>"""
    attributes: (
        "aws_sdk_qconnect.types.message_template_attributes.MessageTemplateAttributes"
    )
    """<p>An object that specifies the values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the value for that variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenderMessageTemplateRequest) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.message_template_attributes

    out["attributes"] = (
        aws_sdk_qconnect.types.message_template_attributes.serialize_json(
            value["attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> RenderMessageTemplateRequest:
    out: RenderMessageTemplateRequest = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_qconnect.types.message_template_attributes

        out["attributes"] = (
            aws_sdk_qconnect.types.message_template_attributes.deserialize_json(
                data["attributes"]
            )
        )
    else:
        raise DeserializationError("RenderMessageTemplateRequest.attributes required")
    return out
