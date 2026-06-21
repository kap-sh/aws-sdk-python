"""Generated from Smithy shape ``com.amazonaws.polly#Engine``."""

from typing import Literal, TypeAlias, cast

Engine: TypeAlias = Literal[
    "standard",
    "neural",
    "long-form",
    "generative",
]


# --- restJson1 ser/de ---
def serialize_json(value: Engine) -> str:
    return value


def deserialize_json(data: str) -> Engine:
    return cast(Engine, data)
