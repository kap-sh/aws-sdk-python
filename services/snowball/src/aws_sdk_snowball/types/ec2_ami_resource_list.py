"""Generated from Smithy shape ``com.amazonaws.snowball#Ec2AmiResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.ec2_ami_resource

Ec2AmiResourceList: TypeAlias = list[
    "aws_sdk_snowball.types.ec2_ami_resource.Ec2AmiResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2AmiResourceList) -> list:
    import aws_sdk_snowball.types.ec2_ami_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_snowball.types.ec2_ami_resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Ec2AmiResourceList:
    import aws_sdk_snowball.types.ec2_ami_resource

    out: Ec2AmiResourceList = []
    for item in data:
        out.append(
            aws_sdk_snowball.types.ec2_ami_resource.deserialize_aws_json_1_1(item)
        )
    return out
