"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProcessingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

ProcessingType: TypeAlias = Literal[
    "CONSISTENT",
    "EVENTUAL",
    "EVENTUAL_NO_LOOKUP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONSISTENT",
        "EVENTUAL",
        "EVENTUAL_NO_LOOKUP",
    )
)


def serialize_json(value: ProcessingType) -> str:
    return value


def deserialize_json(data: str) -> ProcessingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcessingType value: {data!r}")
    return cast(ProcessingType, data)
