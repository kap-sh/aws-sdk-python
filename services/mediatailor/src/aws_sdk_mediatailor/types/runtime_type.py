"""Generated from Smithy shape ``com.amazonaws.mediatailor#RuntimeType``."""

from typing import Literal, TypeAlias, cast

RuntimeType: TypeAlias = Literal["JSONATA",]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeType) -> str:
    return value


def deserialize_json(data: str) -> RuntimeType:
    return cast(RuntimeType, data)
