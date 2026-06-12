"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAssociationStatusInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_association_status_info

InstanceAssociationStatusInfos: TypeAlias = list[
    "aws_sdk_ssm.types.instance_association_status_info.InstanceAssociationStatusInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAssociationStatusInfos) -> list:
    import aws_sdk_ssm.types.instance_association_status_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.instance_association_status_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceAssociationStatusInfos:
    import aws_sdk_ssm.types.instance_association_status_info

    out: InstanceAssociationStatusInfos = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.instance_association_status_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
