"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EmbeddingDataType``."""

from typing import Literal, TypeAlias, cast

"""<p>Bedrock models embedding data type. Can be either float32 or binary.</p>"""
EmbeddingDataType: TypeAlias = Literal[
    "FLOAT32",
    "BINARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddingDataType) -> str:
    return value


def deserialize_json(data: str) -> EmbeddingDataType:
    return cast(EmbeddingDataType, data)
