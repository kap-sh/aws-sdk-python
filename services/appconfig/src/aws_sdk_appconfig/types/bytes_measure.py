"""Generated from Smithy shape ``com.amazonaws.appconfig#BytesMeasure``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

BytesMeasure: TypeAlias = Literal["KILOBYTES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KILOBYTES",))


def serialize_json(value: BytesMeasure) -> str:
    return value


def deserialize_json(data: str) -> BytesMeasure:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BytesMeasure value: {data!r}")
    return cast(BytesMeasure, data)
