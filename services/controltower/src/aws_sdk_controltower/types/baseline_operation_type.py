"""Generated from Smithy shape ``com.amazonaws.controltower#BaselineOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

BaselineOperationType: TypeAlias = Literal[
    "ENABLE_BASELINE",
    "DISABLE_BASELINE",
    "UPDATE_ENABLED_BASELINE",
    "RESET_ENABLED_BASELINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE_BASELINE",
        "DISABLE_BASELINE",
        "UPDATE_ENABLED_BASELINE",
        "RESET_ENABLED_BASELINE",
    )
)


def serialize_json(value: BaselineOperationType) -> str:
    return value


def deserialize_json(data: str) -> BaselineOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BaselineOperationType value: {data!r}")
    return cast(BaselineOperationType, data)
