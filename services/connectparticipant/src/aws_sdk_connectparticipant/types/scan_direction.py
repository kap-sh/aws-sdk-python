"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ScanDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connectparticipant.errors import DeserializationError

ScanDirection: TypeAlias = Literal[
    "FORWARD",
    "BACKWARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FORWARD",
        "BACKWARD",
    )
)


def serialize_json(value: ScanDirection) -> str:
    return value


def deserialize_json(data: str) -> ScanDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanDirection value: {data!r}")
    return cast(ScanDirection, data)
