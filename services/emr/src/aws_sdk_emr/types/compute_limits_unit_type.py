"""Generated from Smithy shape ``com.amazonaws.emr#ComputeLimitsUnitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

ComputeLimitsUnitType: TypeAlias = Literal[
    "InstanceFleetUnits",
    "Instances",
    "VCPU",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceFleetUnits",
        "Instances",
        "VCPU",
    )
)


def serialize_aws_json_1_1(value: ComputeLimitsUnitType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeLimitsUnitType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeLimitsUnitType value: {data!r}")
    return cast(ComputeLimitsUnitType, data)
