"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersion``."""

from typing import Literal, TypeAlias, cast

FunctionVersion: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionVersion) -> str:
    return value


def deserialize_json(data: str) -> FunctionVersion:
    return cast(FunctionVersion, data)
