"""Generated from Smithy shape ``com.amazonaws.backup#RestoreValidationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

RestoreValidationStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCESSFUL",
    "TIMED_OUT",
    "VALIDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SUCCESSFUL",
        "TIMED_OUT",
        "VALIDATING",
    )
)


def serialize_json(value: RestoreValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> RestoreValidationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RestoreValidationStatus value: {data!r}")
    return cast(RestoreValidationStatus, data)
