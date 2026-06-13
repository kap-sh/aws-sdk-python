"""Generated from Smithy shape ``com.amazonaws.quicksight#QDataKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

QDataKeyType: TypeAlias = Literal[
    "AWS_OWNED",
    "CMK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED",
        "CMK",
    )
)


def serialize_json(value: QDataKeyType) -> str:
    return value


def deserialize_json(data: str) -> QDataKeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QDataKeyType value: {data!r}")
    return cast(QDataKeyType, data)
