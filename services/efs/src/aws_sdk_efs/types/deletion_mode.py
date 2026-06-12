"""Generated from Smithy shape ``com.amazonaws.efs#DeletionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

DeletionMode: TypeAlias = Literal[
    "ALL_CONFIGURATIONS",
    "LOCAL_CONFIGURATION_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_CONFIGURATIONS",
        "LOCAL_CONFIGURATION_ONLY",
    )
)


def serialize_json(value: DeletionMode) -> str:
    return value


def deserialize_json(data: str) -> DeletionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeletionMode value: {data!r}")
    return cast(DeletionMode, data)
