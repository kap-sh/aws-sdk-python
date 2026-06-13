"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

AsyncInvokeStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
    )
)


def serialize_json(value: AsyncInvokeStatus) -> str:
    return value


def deserialize_json(data: str) -> AsyncInvokeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AsyncInvokeStatus value: {data!r}")
    return cast(AsyncInvokeStatus, data)
