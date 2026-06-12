"""Generated from Smithy shape ``com.amazonaws.health#entityStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

entityStatusCode: TypeAlias = Literal[
    "IMPAIRED",
    "UNIMPAIRED",
    "UNKNOWN",
    "PENDING",
    "RESOLVED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMPAIRED",
        "UNIMPAIRED",
        "UNKNOWN",
        "PENDING",
        "RESOLVED",
    )
)


def serialize_aws_json_1_1(value: entityStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> entityStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown entityStatusCode value: {data!r}")
    return cast(entityStatusCode, data)
