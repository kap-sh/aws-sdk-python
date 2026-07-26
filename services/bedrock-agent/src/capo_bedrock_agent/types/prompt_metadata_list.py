"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_metadata_entry

PromptMetadataList: TypeAlias = list[
    "capo_bedrock_agent.types.prompt_metadata_entry.PromptMetadataEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptMetadataList) -> list:
    import capo_bedrock_agent.types.prompt_metadata_entry

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.prompt_metadata_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptMetadataList:
    import capo_bedrock_agent.types.prompt_metadata_entry

    out: PromptMetadataList = []
    for item in data:
        out.append(
            capo_bedrock_agent.types.prompt_metadata_entry.deserialize_json(item)
        )
    return out
