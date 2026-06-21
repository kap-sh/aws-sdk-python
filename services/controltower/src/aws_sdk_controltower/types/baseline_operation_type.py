"""Generated from Smithy shape ``com.amazonaws.controltower#BaselineOperationType``."""

from typing import Literal, TypeAlias, cast

BaselineOperationType: TypeAlias = Literal[
    "ENABLE_BASELINE",
    "DISABLE_BASELINE",
    "UPDATE_ENABLED_BASELINE",
    "RESET_ENABLED_BASELINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BaselineOperationType) -> str:
    return value


def deserialize_json(data: str) -> BaselineOperationType:
    return cast(BaselineOperationType, data)
