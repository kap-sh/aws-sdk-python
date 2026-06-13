"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionBlockType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

ExecutionBlockType: TypeAlias = Literal[
    "CustomActionLambda",
    "ManualApproval",
    "AuroraGlobalDatabase",
    "EC2AutoScaling",
    "ARCRoutingControl",
    "ARCRegionSwitchPlan",
    "Parallel",
    "ECSServiceScaling",
    "EKSResourceScaling",
    "Route53HealthCheck",
    "DocumentDb",
    "RdsPromoteReadReplica",
    "RdsCreateCrossRegionReplica",
    "LambdaEventSourceMapping",
    "AuroraServerlessScaling",
    "AuroraProvisionedScaling",
    "NeptuneGlobalDatabase",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CustomActionLambda",
        "ManualApproval",
        "AuroraGlobalDatabase",
        "EC2AutoScaling",
        "ARCRoutingControl",
        "ARCRegionSwitchPlan",
        "Parallel",
        "ECSServiceScaling",
        "EKSResourceScaling",
        "Route53HealthCheck",
        "DocumentDb",
        "RdsPromoteReadReplica",
        "RdsCreateCrossRegionReplica",
        "LambdaEventSourceMapping",
        "AuroraServerlessScaling",
        "AuroraProvisionedScaling",
        "NeptuneGlobalDatabase",
    )
)


def serialize_aws_json_1_0(value: ExecutionBlockType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionBlockType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionBlockType value: {data!r}")
    return cast(ExecutionBlockType, data)
