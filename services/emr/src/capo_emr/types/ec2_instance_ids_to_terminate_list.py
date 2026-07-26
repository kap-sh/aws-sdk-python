"""Generated from Smithy shape ``com.amazonaws.emr#EC2InstanceIdsToTerminateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.instance_id

EC2InstanceIdsToTerminateList: TypeAlias = list["capo_emr.types.instance_id.InstanceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceIdsToTerminateList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EC2InstanceIdsToTerminateList:
    return list(data)
