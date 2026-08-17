"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_id

InstanceIdList: TypeAlias = list["capo_ssm.types.instance_id.InstanceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceIdList:
    return [item for item in data if item is not None]
