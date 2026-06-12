"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_name

InstanceNameList: TypeAlias = list[
    "aws_sdk_codedeploy.types.instance_name.InstanceName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceNameList:
    return list(data)
