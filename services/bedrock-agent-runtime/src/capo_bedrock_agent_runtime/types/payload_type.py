"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PayloadType``."""

from typing import Literal, TypeAlias, cast

PayloadType: TypeAlias = Literal[
    "TEXT",
    "RETURN_CONTROL",
]


# --- restJson1 ser/de ---
def serialize_json(value: PayloadType) -> str:
    return value


def deserialize_json(data: str) -> PayloadType:
    return cast(PayloadType, data)
