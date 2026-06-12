"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#RespondsTo``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_identity.errors import DeserializationError

RespondsTo: TypeAlias = Literal["STANDARD_MESSAGES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STANDARD_MESSAGES",))


def serialize_json(value: RespondsTo) -> str:
    return value


def deserialize_json(data: str) -> RespondsTo:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RespondsTo value: {data!r}")
    return cast(RespondsTo, data)
