"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Ec2AsgCapacityMonitoringApproach``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

Ec2AsgCapacityMonitoringApproach: TypeAlias = Literal[
    "sampledMaxInLast24Hours",
    "autoscalingMaxInLast24Hours",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sampledMaxInLast24Hours",
        "autoscalingMaxInLast24Hours",
    )
)


def serialize_aws_json_1_0(value: Ec2AsgCapacityMonitoringApproach) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Ec2AsgCapacityMonitoringApproach:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Ec2AsgCapacityMonitoringApproach value: {data!r}"
        )
    return cast(Ec2AsgCapacityMonitoringApproach, data)
