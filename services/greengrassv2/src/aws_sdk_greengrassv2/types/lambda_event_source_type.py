"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaEventSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

LambdaEventSourceType: TypeAlias = Literal[
    "PUB_SUB",
    "IOT_CORE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUB_SUB",
        "IOT_CORE",
    )
)


def serialize_json(value: LambdaEventSourceType) -> str:
    return value


def deserialize_json(data: str) -> LambdaEventSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LambdaEventSourceType value: {data!r}")
    return cast(LambdaEventSourceType, data)
