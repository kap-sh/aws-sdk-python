"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryRecordSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.metadata_schema_list


class MemoryRecordSchema(TypedDict):
    metadata_schema: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.metadata_schema_list.MetadataSchemaList"
    ]
    """<p>The metadata field definitions for this strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordSchema) -> dict:
    out: dict = {}
    if "metadata_schema" in value:
        import aws_sdk_bedrock_agentcore_control.types.metadata_schema_list

        out["metadataSchema"] = (
            aws_sdk_bedrock_agentcore_control.types.metadata_schema_list.serialize_json(
                value["metadata_schema"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryRecordSchema:
    out: MemoryRecordSchema = {}  # type: ignore[typeddict-item]
    if "metadataSchema" in data:
        import aws_sdk_bedrock_agentcore_control.types.metadata_schema_list

        out["metadata_schema"] = (
            aws_sdk_bedrock_agentcore_control.types.metadata_schema_list.deserialize_json(
                data["metadataSchema"]
            )
        )
    return out
