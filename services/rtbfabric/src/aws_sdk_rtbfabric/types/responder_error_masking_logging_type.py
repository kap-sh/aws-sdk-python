"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderErrorMaskingLoggingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

ResponderErrorMaskingLoggingType: TypeAlias = Literal[
    "NONE",
    "METRIC",
    "RESPONSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "METRIC",
        "RESPONSE",
    )
)


def serialize_json(value: ResponderErrorMaskingLoggingType) -> str:
    return value


def deserialize_json(data: str) -> ResponderErrorMaskingLoggingType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResponderErrorMaskingLoggingType value: {data!r}"
        )
    return cast(ResponderErrorMaskingLoggingType, data)
