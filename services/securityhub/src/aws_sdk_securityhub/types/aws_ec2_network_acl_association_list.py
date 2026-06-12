"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkAclAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_network_acl_association

AwsEc2NetworkAclAssociationList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ec2_network_acl_association.AwsEc2NetworkAclAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkAclAssociationList) -> list:
    import aws_sdk_securityhub.types.aws_ec2_network_acl_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_network_acl_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEc2NetworkAclAssociationList:
    import aws_sdk_securityhub.types.aws_ec2_network_acl_association

    out: AwsEc2NetworkAclAssociationList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ec2_network_acl_association.deserialize_json(
                item
            )
        )
    return out
