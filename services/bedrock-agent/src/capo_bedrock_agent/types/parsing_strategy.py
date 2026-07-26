"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ParsingStrategy``."""

from typing import Literal, TypeAlias, cast

ParsingStrategy: TypeAlias = Literal[
    "BEDROCK_FOUNDATION_MODEL",
    "BEDROCK_DATA_AUTOMATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParsingStrategy) -> str:
    return value


def deserialize_json(data: str) -> ParsingStrategy:
    return cast(ParsingStrategy, data)
