"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryRecordSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.metadata_schema_list


class MemoryRecordSchema(TypedDict, closed=True):
    metadata_schema: NotRequired[
        "capo_bedrock_agentcore_control.types.metadata_schema_list.MetadataSchemaList"
    ]
    """<p>The metadata field definitions for this strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordSchema) -> dict:
    out: dict = {}
    if "metadata_schema" in value:
        import capo_bedrock_agentcore_control.types.metadata_schema_list

        out["metadataSchema"] = (
            capo_bedrock_agentcore_control.types.metadata_schema_list.serialize_json(
                value["metadata_schema"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryRecordSchema:
    out: MemoryRecordSchema = {}  # type: ignore[typeddict-item]
    if "metadataSchema" in data:
        import capo_bedrock_agentcore_control.types.metadata_schema_list

        out["metadata_schema"] = (
            capo_bedrock_agentcore_control.types.metadata_schema_list.deserialize_json(
                data["metadataSchema"]
            )
        )
    return out
