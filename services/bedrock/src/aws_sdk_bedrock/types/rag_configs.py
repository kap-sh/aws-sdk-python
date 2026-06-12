"""Generated from Smithy shape ``com.amazonaws.bedrock#RagConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.rag_config

RagConfigs: TypeAlias = list["aws_sdk_bedrock.types.rag_config.RAGConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: RagConfigs) -> list:
    import aws_sdk_bedrock.types.rag_config

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.rag_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> RagConfigs:
    import aws_sdk_bedrock.types.rag_config

    out: RagConfigs = []
    for item in data:
        out.append(aws_sdk_bedrock.types.rag_config.deserialize_json(item))
    return out
