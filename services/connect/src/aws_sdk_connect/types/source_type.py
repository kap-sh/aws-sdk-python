"""Generated from Smithy shape ``com.amazonaws.connect#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "SALESFORCE",
    "ZENDESK",
    "CASES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SALESFORCE",
        "ZENDESK",
        "CASES",
    )
)


def serialize_json(value: SourceType) -> str:
    return value


def deserialize_json(data: str) -> SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {data!r}")
    return cast(SourceType, data)
