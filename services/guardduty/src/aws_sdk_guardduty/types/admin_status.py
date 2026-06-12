"""Generated from Smithy shape ``com.amazonaws.guardduty#AdminStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

AdminStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLE_IN_PROGRESS",
    )
)


def serialize_json(value: AdminStatus) -> str:
    return value


def deserialize_json(data: str) -> AdminStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdminStatus value: {data!r}")
    return cast(AdminStatus, data)
