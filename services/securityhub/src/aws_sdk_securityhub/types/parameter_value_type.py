"""Generated from Smithy shape ``com.amazonaws.securityhub#ParameterValueType``."""

from typing import Literal, TypeAlias, cast

ParameterValueType: TypeAlias = Literal[
    "DEFAULT",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterValueType) -> str:
    return value


def deserialize_json(data: str) -> ParameterValueType:
    return cast(ParameterValueType, data)
