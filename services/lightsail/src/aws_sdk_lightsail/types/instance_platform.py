"""Generated from Smithy shape ``com.amazonaws.lightsail#InstancePlatform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

InstancePlatform: TypeAlias = Literal[
    "LINUX_UNIX",
    "WINDOWS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINUX_UNIX",
        "WINDOWS",
    )
)


def serialize_aws_json_1_1(value: InstancePlatform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstancePlatform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstancePlatform value: {data!r}")
    return cast(InstancePlatform, data)
