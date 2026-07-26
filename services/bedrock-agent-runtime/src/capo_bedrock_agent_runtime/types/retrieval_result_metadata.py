"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieval_result_metadata_key
    import capo_bedrock_agent_runtime.types.retrieval_result_metadata_value

RetrievalResultMetadata: TypeAlias = dict[
    "capo_bedrock_agent_runtime.types.retrieval_result_metadata_key.RetrievalResultMetadataKey",
    "capo_bedrock_agent_runtime.types.retrieval_result_metadata_value.RetrievalResultMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RetrievalResultMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RetrievalResultMetadata:
    out: RetrievalResultMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
