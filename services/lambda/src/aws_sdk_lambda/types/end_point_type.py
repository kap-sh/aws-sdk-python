"""Generated from Smithy shape ``com.amazonaws.lambda#EndPointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

EndPointType: TypeAlias = Literal["KAFKA_BOOTSTRAP_SERVERS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KAFKA_BOOTSTRAP_SERVERS",))


def serialize_json(value: EndPointType) -> str:
    return value


def deserialize_json(data: str) -> EndPointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndPointType value: {data!r}")
    return cast(EndPointType, data)
