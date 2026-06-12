"""Generated from Smithy shape ``com.amazonaws.novaact#ModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_nova_act.errors import DeserializationError

ModelStatus: TypeAlias = Literal[
    "ACTIVE",
    "LEGACY",
    "DEPRECATED",
    "PREVIEW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "LEGACY",
        "DEPRECATED",
        "PREVIEW",
    )
)


def serialize_json(value: ModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelStatus value: {data!r}")
    return cast(ModelStatus, data)
