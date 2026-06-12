"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetGroupPairInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.target_group_pair_info

TargetGroupPairInfoList: TypeAlias = list[
    "aws_sdk_codedeploy.types.target_group_pair_info.TargetGroupPairInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetGroupPairInfoList) -> list:
    import aws_sdk_codedeploy.types.target_group_pair_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.target_group_pair_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetGroupPairInfoList:
    import aws_sdk_codedeploy.types.target_group_pair_info

    out: TargetGroupPairInfoList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.target_group_pair_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
