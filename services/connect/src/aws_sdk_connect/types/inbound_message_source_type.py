"""Generated from Smithy shape ``com.amazonaws.connect#InboundMessageSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

InboundMessageSourceType: TypeAlias = Literal["RAW",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RAW",))


def serialize_json(value: InboundMessageSourceType) -> str:
    return value


def deserialize_json(data: str) -> InboundMessageSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InboundMessageSourceType value: {data!r}")
    return cast(InboundMessageSourceType, data)
