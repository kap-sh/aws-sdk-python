"""Generated from Smithy shape ``com.amazonaws.lightsail#CloudFormationStackRecordSourceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.cloud_formation_stack_record_source_info

CloudFormationStackRecordSourceInfoList: TypeAlias = list[
    "capo_lightsail.types.cloud_formation_stack_record_source_info.CloudFormationStackRecordSourceInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudFormationStackRecordSourceInfoList) -> list:
    import capo_lightsail.types.cloud_formation_stack_record_source_info

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.cloud_formation_stack_record_source_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CloudFormationStackRecordSourceInfoList:
    import capo_lightsail.types.cloud_formation_stack_record_source_info

    out: CloudFormationStackRecordSourceInfoList = []
    for item in data:
        out.append(
            capo_lightsail.types.cloud_formation_stack_record_source_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
