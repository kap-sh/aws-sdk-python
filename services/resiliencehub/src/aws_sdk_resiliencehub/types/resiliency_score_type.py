"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResiliencyScoreType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ResiliencyScoreType: TypeAlias = Literal[
    "Compliance",
    "Test",
    "Alarm",
    "Sop",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Compliance",
        "Test",
        "Alarm",
        "Sop",
    )
)


def serialize_json(value: ResiliencyScoreType) -> str:
    return value


def deserialize_json(data: str) -> ResiliencyScoreType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResiliencyScoreType value: {data!r}")
    return cast(ResiliencyScoreType, data)
