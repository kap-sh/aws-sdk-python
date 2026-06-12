"""Generated from Smithy shape ``com.amazonaws.synthetics#ResourceToTag``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

ResourceToTag: TypeAlias = Literal["lambda-function",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("lambda-function",))


def serialize_json(value: ResourceToTag) -> str:
    return value


def deserialize_json(data: str) -> ResourceToTag:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceToTag value: {data!r}")
    return cast(ResourceToTag, data)
