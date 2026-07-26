"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#InterpretationSource``."""

from typing import Literal, TypeAlias, cast

InterpretationSource: TypeAlias = Literal[
    "Bedrock",
    "Lex",
]


# --- restJson1 ser/de ---
def serialize_json(value: InterpretationSource) -> str:
    return value


def deserialize_json(data: str) -> InterpretationSource:
    return cast(InterpretationSource, data)
