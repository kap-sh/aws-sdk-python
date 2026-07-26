"""Generated from Smithy shape ``com.amazonaws.mediatailor#FunctionType``."""

from typing import Literal, TypeAlias, cast

"""-- Define Enums"""
FunctionType: TypeAlias = Literal[
    "HTTP_REQUEST",
    "CUSTOM_OUTPUT",
    "SEQUENTIAL_EXECUTOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionType) -> str:
    return value


def deserialize_json(data: str) -> FunctionType:
    return cast(FunctionType, data)
