"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

RuleType: TypeAlias = Literal[
    "BINARY_LENGTH",
    "NUMBER_COMPARISON",
    "STRING_FROM_SET",
    "STRING_LENGTH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BINARY_LENGTH",
        "NUMBER_COMPARISON",
        "STRING_FROM_SET",
        "STRING_LENGTH",
    )
)


def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleType value: {data!r}")
    return cast(RuleType, data)
