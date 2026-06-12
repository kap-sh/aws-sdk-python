"""Generated from Smithy shape ``com.amazonaws.mediatailor#RuntimeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

RuntimeType: TypeAlias = Literal["JSONATA",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("JSONATA",))


def serialize_json(value: RuntimeType) -> str:
    return value


def deserialize_json(data: str) -> RuntimeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuntimeType value: {data!r}")
    return cast(RuntimeType, data)
