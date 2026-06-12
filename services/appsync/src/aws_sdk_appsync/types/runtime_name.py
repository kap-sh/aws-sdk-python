"""Generated from Smithy shape ``com.amazonaws.appsync#RuntimeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

RuntimeName: TypeAlias = Literal["APPSYNC_JS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("APPSYNC_JS",))


def serialize_json(value: RuntimeName) -> str:
    return value


def deserialize_json(data: str) -> RuntimeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuntimeName value: {data!r}")
    return cast(RuntimeName, data)
