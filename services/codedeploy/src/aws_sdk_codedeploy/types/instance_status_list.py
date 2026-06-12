"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_status

InstanceStatusList: TypeAlias = list[
    "aws_sdk_codedeploy.types.instance_status.InstanceStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStatusList) -> list:
    import aws_sdk_codedeploy.types.instance_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.instance_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceStatusList:
    import aws_sdk_codedeploy.types.instance_status

    out: InstanceStatusList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.instance_status.deserialize_aws_json_1_1(item)
        )
    return out
