"""Generated from Smithy shape ``com.amazonaws.devicefarm#AuxiliaryAppArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name

AuxiliaryAppArnList: TypeAlias = list[
    "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuxiliaryAppArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AuxiliaryAppArnList:
    return list(data)
