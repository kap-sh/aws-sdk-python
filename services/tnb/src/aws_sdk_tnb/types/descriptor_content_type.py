"""Generated from Smithy shape ``com.amazonaws.tnb#DescriptorContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

DescriptorContentType: TypeAlias = Literal["text/plain",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("text/plain",))


def serialize_json(value: DescriptorContentType) -> str:
    return value


def deserialize_json(data: str) -> DescriptorContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DescriptorContentType value: {data!r}")
    return cast(DescriptorContentType, data)
