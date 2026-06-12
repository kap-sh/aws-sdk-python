"""Generated from Smithy shape ``com.amazonaws.backupgateway#Hypervisors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.hypervisor

Hypervisors: TypeAlias = list["aws_sdk_backup_gateway.types.hypervisor.Hypervisor"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Hypervisors) -> list:
    import aws_sdk_backup_gateway.types.hypervisor

    out: list = []
    for item in value:
        out.append(aws_sdk_backup_gateway.types.hypervisor.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Hypervisors:
    import aws_sdk_backup_gateway.types.hypervisor

    out: Hypervisors = []
    for item in data:
        out.append(
            aws_sdk_backup_gateway.types.hypervisor.deserialize_aws_json_1_0(item)
        )
    return out
