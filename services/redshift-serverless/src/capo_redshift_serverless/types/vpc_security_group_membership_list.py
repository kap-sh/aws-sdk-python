"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#VpcSecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.vpc_security_group_membership

VpcSecurityGroupMembershipList: TypeAlias = list[
    "capo_redshift_serverless.types.vpc_security_group_membership.VpcSecurityGroupMembership"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcSecurityGroupMembershipList) -> list:
    import capo_redshift_serverless.types.vpc_security_group_membership

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.vpc_security_group_membership.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VpcSecurityGroupMembershipList:
    import capo_redshift_serverless.types.vpc_security_group_membership

    out: VpcSecurityGroupMembershipList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.vpc_security_group_membership.deserialize_aws_json_1_1(
                item
            )
        )
    return out
