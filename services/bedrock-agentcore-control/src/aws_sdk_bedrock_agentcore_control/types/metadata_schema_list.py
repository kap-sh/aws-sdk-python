"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MetadataSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.metadata_schema_entry

MetadataSchemaList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.metadata_schema_entry.MetadataSchemaEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataSchemaList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.metadata_schema_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.metadata_schema_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetadataSchemaList:
    import aws_sdk_bedrock_agentcore_control.types.metadata_schema_entry

    out: MetadataSchemaList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.metadata_schema_entry.deserialize_json(
                item
            )
        )
    return out
