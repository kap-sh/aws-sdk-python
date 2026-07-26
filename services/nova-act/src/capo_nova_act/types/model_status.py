"""Generated from Smithy shape ``com.amazonaws.novaact#ModelStatus``."""

from typing import Literal, TypeAlias, cast

ModelStatus: TypeAlias = Literal[
    "ACTIVE",
    "LEGACY",
    "DEPRECATED",
    "PREVIEW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelStatus:
    return cast(ModelStatus, data)
