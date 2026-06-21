"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExceptionLevel``."""

from typing import Literal, TypeAlias, cast

ExceptionLevel: TypeAlias = Literal["DEBUG",]


# --- restJson1 ser/de ---
def serialize_json(value: ExceptionLevel) -> str:
    return value


def deserialize_json(data: str) -> ExceptionLevel:
    return cast(ExceptionLevel, data)
