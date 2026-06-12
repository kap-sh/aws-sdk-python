"""Generated from Smithy shape ``com.amazonaws.lightsail#HttpEndpoint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

HttpEndpoint: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
    )
)


def serialize_aws_json_1_1(value: HttpEndpoint) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HttpEndpoint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HttpEndpoint value: {data!r}")
    return cast(HttpEndpoint, data)
