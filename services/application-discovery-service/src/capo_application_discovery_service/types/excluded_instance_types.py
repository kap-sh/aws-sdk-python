"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExcludedInstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.ec2_instance_type

ExcludedInstanceTypes: TypeAlias = list[
    "capo_application_discovery_service.types.ec2_instance_type.EC2InstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludedInstanceTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludedInstanceTypes:
    return list(data)
