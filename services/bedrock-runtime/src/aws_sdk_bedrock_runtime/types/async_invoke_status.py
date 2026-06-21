"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeStatus``."""

from typing import Literal, TypeAlias, cast

AsyncInvokeStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: AsyncInvokeStatus) -> str:
    return value


def deserialize_json(data: str) -> AsyncInvokeStatus:
    return cast(AsyncInvokeStatus, data)
