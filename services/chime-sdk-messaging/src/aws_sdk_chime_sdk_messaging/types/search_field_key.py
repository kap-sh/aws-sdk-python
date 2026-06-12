"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchFieldKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

SearchFieldKey: TypeAlias = Literal["MEMBERS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MEMBERS",))


def serialize_json(value: SearchFieldKey) -> str:
    return value


def deserialize_json(data: str) -> SearchFieldKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchFieldKey value: {data!r}")
    return cast(SearchFieldKey, data)
