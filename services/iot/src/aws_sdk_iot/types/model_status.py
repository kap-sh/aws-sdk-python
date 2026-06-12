"""Generated from Smithy shape ``com.amazonaws.iot#ModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ModelStatus: TypeAlias = Literal[
    "PENDING_BUILD",
    "ACTIVE",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_BUILD",
        "ACTIVE",
        "EXPIRED",
    )
)


def serialize_json(value: ModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelStatus value: {data!r}")
    return cast(ModelStatus, data)
