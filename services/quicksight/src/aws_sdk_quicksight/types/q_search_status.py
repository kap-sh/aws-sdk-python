"""Generated from Smithy shape ``com.amazonaws.quicksight#QSearchStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

QSearchStatus: TypeAlias = Literal[
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


def serialize_json(value: QSearchStatus) -> str:
    return value


def deserialize_json(data: str) -> QSearchStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QSearchStatus value: {data!r}")
    return cast(QSearchStatus, data)
