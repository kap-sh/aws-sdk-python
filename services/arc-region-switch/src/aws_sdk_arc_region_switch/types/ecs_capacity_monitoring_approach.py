"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EcsCapacityMonitoringApproach``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

EcsCapacityMonitoringApproach: TypeAlias = Literal[
    "sampledMaxInLast24Hours",
    "containerInsightsMaxInLast24Hours",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sampledMaxInLast24Hours",
        "containerInsightsMaxInLast24Hours",
    )
)


def serialize_aws_json_1_0(value: EcsCapacityMonitoringApproach) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EcsCapacityMonitoringApproach:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EcsCapacityMonitoringApproach value: {data!r}"
        )
    return cast(EcsCapacityMonitoringApproach, data)
