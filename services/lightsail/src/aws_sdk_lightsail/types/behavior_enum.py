"""Generated from Smithy shape ``com.amazonaws.lightsail#BehaviorEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

BehaviorEnum: TypeAlias = Literal[
    "dont-cache",
    "cache",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "dont-cache",
        "cache",
    )
)


def serialize_aws_json_1_1(value: BehaviorEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BehaviorEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BehaviorEnum value: {data!r}")
    return cast(BehaviorEnum, data)
