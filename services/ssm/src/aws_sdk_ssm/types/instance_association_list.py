"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_association

InstanceAssociationList: TypeAlias = list[
    "aws_sdk_ssm.types.instance_association.InstanceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAssociationList) -> list:
    import aws_sdk_ssm.types.instance_association

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.instance_association.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceAssociationList:
    import aws_sdk_ssm.types.instance_association

    out: InstanceAssociationList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.instance_association.deserialize_aws_json_1_1(item)
        )
    return out
