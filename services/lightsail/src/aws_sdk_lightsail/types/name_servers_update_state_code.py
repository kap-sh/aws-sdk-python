"""Generated from Smithy shape ``com.amazonaws.lightsail#NameServersUpdateStateCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

NameServersUpdateStateCode: TypeAlias = Literal[
    "SUCCEEDED",
    "PENDING",
    "FAILED",
    "STARTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "PENDING",
        "FAILED",
        "STARTED",
    )
)


def serialize_aws_json_1_1(value: NameServersUpdateStateCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NameServersUpdateStateCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NameServersUpdateStateCode value: {data!r}"
        )
    return cast(NameServersUpdateStateCode, data)
