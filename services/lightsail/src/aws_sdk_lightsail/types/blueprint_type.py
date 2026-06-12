"""Generated from Smithy shape ``com.amazonaws.lightsail#BlueprintType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

BlueprintType: TypeAlias = Literal[
    "os",
    "app",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "os",
        "app",
    )
)


def serialize_aws_json_1_1(value: BlueprintType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlueprintType value: {data!r}")
    return cast(BlueprintType, data)
