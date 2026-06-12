"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_information

InstanceInformationList: TypeAlias = list[
    "aws_sdk_ssm.types.instance_information.InstanceInformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInformationList) -> list:
    import aws_sdk_ssm.types.instance_information

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.instance_information.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceInformationList:
    import aws_sdk_ssm.types.instance_information

    out: InstanceInformationList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.instance_information.deserialize_aws_json_1_1(item)
        )
    return out
