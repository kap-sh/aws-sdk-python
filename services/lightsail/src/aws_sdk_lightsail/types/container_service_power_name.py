"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServicePowerName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContainerServicePowerName: TypeAlias = Literal[
    "nano",
    "micro",
    "small",
    "medium",
    "large",
    "xlarge",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "nano",
        "micro",
        "small",
        "medium",
        "large",
        "xlarge",
    )
)


def serialize_aws_json_1_1(value: ContainerServicePowerName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServicePowerName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerServicePowerName value: {data!r}")
    return cast(ContainerServicePowerName, data)
