"""Generated from Smithy shape ``com.amazonaws.iot#ModelStatus``."""

from typing import Literal, TypeAlias, cast

ModelStatus: TypeAlias = Literal[
    "PENDING_BUILD",
    "ACTIVE",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelStatus:
    return cast(ModelStatus, data)
