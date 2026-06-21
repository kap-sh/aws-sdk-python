"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ParsingModality``."""

from typing import Literal, TypeAlias, cast

ParsingModality: TypeAlias = Literal["MULTIMODAL",]


# --- restJson1 ser/de ---
def serialize_json(value: ParsingModality) -> str:
    return value


def deserialize_json(data: str) -> ParsingModality:
    return cast(ParsingModality, data)
