"""Generated from Smithy shape ``com.amazonaws.b2bi#Logging``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

Logging: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: Logging) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Logging:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Logging value: {data!r}")
    return cast(Logging, data)
