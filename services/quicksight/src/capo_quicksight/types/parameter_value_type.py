"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterValueType``."""

from typing import Literal, TypeAlias, cast

ParameterValueType: TypeAlias = Literal[
    "MULTI_VALUED",
    "SINGLE_VALUED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterValueType) -> str:
    return value


def deserialize_json(data: str) -> ParameterValueType:
    return cast(ParameterValueType, data)
