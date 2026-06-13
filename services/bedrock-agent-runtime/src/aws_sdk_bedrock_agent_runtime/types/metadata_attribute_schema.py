"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MetadataAttributeSchema``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.attribute_type


class MetadataAttributeSchema(TypedDict):
    key: "str"
    """<p>The attribute's key.</p>"""
    type: "aws_sdk_bedrock_agent_runtime.types.attribute_type.AttributeType"
    """<p>The attribute's type.</p>"""
    description: "str"
    """<p>The attribute's description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributeSchema) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_bedrock_agent_runtime.types.attribute_type

    out["type"] = aws_sdk_bedrock_agent_runtime.types.attribute_type.serialize_json(
        value["type"]
    )
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> MetadataAttributeSchema:
    out: MetadataAttributeSchema = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("MetadataAttributeSchema.key required")
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.attribute_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.attribute_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("MetadataAttributeSchema.type required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("MetadataAttributeSchema.description required")
    return out
