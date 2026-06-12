"""Generated from Smithy shape ``com.amazonaws.detective#Reason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

Reason: TypeAlias = Literal["AWS_THREAT_INTELLIGENCE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS_THREAT_INTELLIGENCE",))


def serialize_json(value: Reason) -> str:
    return value


def deserialize_json(data: str) -> Reason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Reason value: {data!r}")
    return cast(Reason, data)
