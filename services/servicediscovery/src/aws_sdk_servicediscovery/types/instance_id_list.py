"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InstanceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.resource_id

InstanceIdList: TypeAlias = list[
    "aws_sdk_servicediscovery.types.resource_id.ResourceId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceIdList:
    return list(data)
