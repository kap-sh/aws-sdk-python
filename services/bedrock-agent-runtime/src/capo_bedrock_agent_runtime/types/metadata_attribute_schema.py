"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MetadataAttributeSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.attribute_type


class MetadataAttributeSchema(TypedDict, closed=True):
    key: "str"
    """<p>The attribute's key.</p>"""
    type: "capo_bedrock_agent_runtime.types.attribute_type.AttributeType"
    """<p>The attribute's type.</p>"""
    description: "str"
    """<p>The attribute's description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributeSchema) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bedrock_agent_runtime.types.attribute_type

    out["type"] = capo_bedrock_agent_runtime.types.attribute_type.serialize_json(
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
        import capo_bedrock_agent_runtime.types.attribute_type

        out["type"] = capo_bedrock_agent_runtime.types.attribute_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("MetadataAttributeSchema.type required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("MetadataAttributeSchema.description required")
    return out
