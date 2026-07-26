"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RuleType``."""

from typing import Literal, TypeAlias, cast

RuleType: TypeAlias = Literal[
    "BINARY_LENGTH",
    "NUMBER_COMPARISON",
    "STRING_FROM_SET",
    "STRING_LENGTH",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    return cast(RuleType, data)
