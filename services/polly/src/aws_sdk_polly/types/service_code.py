"""Generated from Smithy shape ``com.amazonaws.polly#ServiceCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

ServiceCode: TypeAlias = Literal["polly",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("polly",))


def serialize_json(value: ServiceCode) -> str:
    return value


def deserialize_json(data: str) -> ServiceCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceCode value: {data!r}")
    return cast(ServiceCode, data)
