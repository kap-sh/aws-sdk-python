"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MetadataSchemaEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.extraction_config
    import aws_sdk_bedrock_agentcore_control.types.extraction_type
    import aws_sdk_bedrock_agentcore_control.types.metadata_key
    import aws_sdk_bedrock_agentcore_control.types.metadata_value_type


class MetadataSchemaEntry(TypedDict, closed=True):
    key: "aws_sdk_bedrock_agentcore_control.types.metadata_key.MetadataKey"
    """<p>The metadata field name. Must match an indexed key to be queryable via metadata filters.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.metadata_value_type.MetadataValueType"
    ]
    """<p>The MetadataValueType.</p>"""
    extraction_type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.extraction_type.ExtractionType"
    ]
    """<p>Specifies whether the metadata value is extracted by the LLM or passed through deterministically from the event.</p>"""
    extraction_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.extraction_config.ExtractionConfig"
    ]
    """<p>Configuration for extracting this metadata value from conversational content. Applicable only if extractionType is LLM inferred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataSchemaEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "type" in value:
        import aws_sdk_bedrock_agentcore_control.types.metadata_value_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.metadata_value_type.serialize_json(
                value["type"]
            )
        )
    if "extraction_type" in value:
        import aws_sdk_bedrock_agentcore_control.types.extraction_type

        out["extractionType"] = (
            aws_sdk_bedrock_agentcore_control.types.extraction_type.serialize_json(
                value["extraction_type"]
            )
        )
    if "extraction_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.extraction_config

        out["extractionConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.extraction_config.serialize_json(
                value["extraction_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataSchemaEntry:
    out: MetadataSchemaEntry = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("MetadataSchemaEntry.key required")
    if "type" in data:
        import aws_sdk_bedrock_agentcore_control.types.metadata_value_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.metadata_value_type.deserialize_json(
                data["type"]
            )
        )
    if "extractionType" in data:
        import aws_sdk_bedrock_agentcore_control.types.extraction_type

        out["extraction_type"] = (
            aws_sdk_bedrock_agentcore_control.types.extraction_type.deserialize_json(
                data["extractionType"]
            )
        )
    if "extractionConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.extraction_config

        out["extraction_config"] = (
            aws_sdk_bedrock_agentcore_control.types.extraction_config.deserialize_json(
                data["extractionConfig"]
            )
        )
    return out
