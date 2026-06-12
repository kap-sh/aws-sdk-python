"""Generated from Smithy shape ``com.amazonaws.emrcontainers#PersistentAppUI``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

PersistentAppUI: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: PersistentAppUI) -> str:
    return value


def deserialize_json(data: str) -> PersistentAppUI:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PersistentAppUI value: {data!r}")
    return cast(PersistentAppUI, data)
