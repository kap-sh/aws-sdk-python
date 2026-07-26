"""Generated from Smithy shape ``com.amazonaws.dax#SecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dax.types.security_group_membership

SecurityGroupMembershipList: TypeAlias = list[
    "capo_dax.types.security_group_membership.SecurityGroupMembership"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupMembershipList) -> list:
    import capo_dax.types.security_group_membership

    out: list = []
    for item in value:
        out.append(
            capo_dax.types.security_group_membership.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityGroupMembershipList:
    import capo_dax.types.security_group_membership

    out: SecurityGroupMembershipList = []
    for item in data:
        out.append(
            capo_dax.types.security_group_membership.deserialize_aws_json_1_1(item)
        )
    return out
