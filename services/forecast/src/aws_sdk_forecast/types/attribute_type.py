"""Generated from Smithy shape ``com.amazonaws.forecast#AttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

AttributeType: TypeAlias = Literal[
    "string",
    "integer",
    "float",
    "timestamp",
    "geolocation",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "string",
        "integer",
        "float",
        "timestamp",
        "geolocation",
    )
)


def serialize_aws_json_1_1(value: AttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeType value: {data!r}")
    return cast(AttributeType, data)
