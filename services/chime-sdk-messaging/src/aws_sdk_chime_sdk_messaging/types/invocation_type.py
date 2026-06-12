"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#InvocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

InvocationType: TypeAlias = Literal["ASYNC",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASYNC",))


def serialize_json(value: InvocationType) -> str:
    return value


def deserialize_json(data: str) -> InvocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvocationType value: {data!r}")
    return cast(InvocationType, data)
