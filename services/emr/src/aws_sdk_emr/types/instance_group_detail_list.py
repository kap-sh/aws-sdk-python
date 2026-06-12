"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_group_detail

InstanceGroupDetailList: TypeAlias = list[
    "aws_sdk_emr.types.instance_group_detail.InstanceGroupDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupDetailList) -> list:
    import aws_sdk_emr.types.instance_group_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.instance_group_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceGroupDetailList:
    import aws_sdk_emr.types.instance_group_detail

    out: InstanceGroupDetailList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.instance_group_detail.deserialize_aws_json_1_1(item)
        )
    return out
