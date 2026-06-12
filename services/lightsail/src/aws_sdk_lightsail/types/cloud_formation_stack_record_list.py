"""Generated from Smithy shape ``com.amazonaws.lightsail#CloudFormationStackRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.cloud_formation_stack_record

CloudFormationStackRecordList: TypeAlias = list[
    "aws_sdk_lightsail.types.cloud_formation_stack_record.CloudFormationStackRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudFormationStackRecordList) -> list:
    import aws_sdk_lightsail.types.cloud_formation_stack_record

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.cloud_formation_stack_record.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CloudFormationStackRecordList:
    import aws_sdk_lightsail.types.cloud_formation_stack_record

    out: CloudFormationStackRecordList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.cloud_formation_stack_record.deserialize_aws_json_1_1(
                item
            )
        )
    return out
