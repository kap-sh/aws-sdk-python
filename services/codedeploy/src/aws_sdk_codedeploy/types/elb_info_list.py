"""Generated from Smithy shape ``com.amazonaws.codedeploy#ELBInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.elb_info

ELBInfoList: TypeAlias = list["aws_sdk_codedeploy.types.elb_info.ELBInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ELBInfoList) -> list:
    import aws_sdk_codedeploy.types.elb_info

    out: list = []
    for item in value:
        out.append(aws_sdk_codedeploy.types.elb_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ELBInfoList:
    import aws_sdk_codedeploy.types.elb_info

    out: ELBInfoList = []
    for item in data:
        out.append(aws_sdk_codedeploy.types.elb_info.deserialize_aws_json_1_1(item))
    return out
