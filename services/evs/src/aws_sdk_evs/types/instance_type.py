"""Generated from Smithy shape ``com.amazonaws.evs#InstanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

InstanceType: TypeAlias = Literal[
    "i4i.metal",
    "i7i.metal-24xl",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "i4i.metal",
        "i7i.metal-24xl",
    )
)


def serialize_aws_json_1_0(value: InstanceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceType value: {data!r}")
    return cast(InstanceType, data)
