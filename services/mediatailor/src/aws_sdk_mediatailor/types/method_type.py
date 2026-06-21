"""Generated from Smithy shape ``com.amazonaws.mediatailor#MethodType``."""

from typing import Literal, TypeAlias, cast

MethodType: TypeAlias = Literal[
    "GET",
    "POST",
]


# --- restJson1 ser/de ---
def serialize_json(value: MethodType) -> str:
    return value


def deserialize_json(data: str) -> MethodType:
    return cast(MethodType, data)
