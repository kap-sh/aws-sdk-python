"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ProtectedJobType: TypeAlias = Literal["PYSPARK",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PYSPARK",))


def serialize_json(value: ProtectedJobType) -> str:
    return value


def deserialize_json(data: str) -> ProtectedJobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtectedJobType value: {data!r}")
    return cast(ProtectedJobType, data)
