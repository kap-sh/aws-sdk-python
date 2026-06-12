"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceMetadataState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

InstanceMetadataState: TypeAlias = Literal[
    "pending",
    "applied",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "applied",
    )
)


def serialize_aws_json_1_1(value: InstanceMetadataState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceMetadataState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceMetadataState value: {data!r}")
    return cast(InstanceMetadataState, data)
