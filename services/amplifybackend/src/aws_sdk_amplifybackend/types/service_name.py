"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ServiceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

ServiceName: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3",))


def serialize_json(value: ServiceName) -> str:
    return value


def deserialize_json(data: str) -> ServiceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceName value: {data!r}")
    return cast(ServiceName, data)
