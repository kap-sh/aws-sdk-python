"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_info

InstanceInfoList: TypeAlias = list[
    "aws_sdk_codedeploy.types.instance_info.InstanceInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInfoList) -> list:
    import aws_sdk_codedeploy.types.instance_info

    out: list = []
    for item in value:
        out.append(aws_sdk_codedeploy.types.instance_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceInfoList:
    import aws_sdk_codedeploy.types.instance_info

    out: InstanceInfoList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.instance_info.deserialize_aws_json_1_1(item)
        )
    return out
