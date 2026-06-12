"""Generated from Smithy shape ``com.amazonaws.securityhub#RecordState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

RecordState: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ARCHIVED",
    )
)


def serialize_json(value: RecordState) -> str:
    return value


def deserialize_json(data: str) -> RecordState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordState value: {data!r}")
    return cast(RecordState, data)
