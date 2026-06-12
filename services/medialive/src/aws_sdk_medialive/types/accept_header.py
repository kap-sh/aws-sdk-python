"""Generated from Smithy shape ``com.amazonaws.medialive#AcceptHeader``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The HTTP Accept header. Indicates the requested type fothe thumbnail."""
AcceptHeader: TypeAlias = Literal["image/jpeg",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("image/jpeg",))


def serialize_json(value: AcceptHeader) -> str:
    return value


def deserialize_json(data: str) -> AcceptHeader:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptHeader value: {data!r}")
    return cast(AcceptHeader, data)
