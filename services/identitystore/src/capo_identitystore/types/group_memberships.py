"""Generated from Smithy shape ``com.amazonaws.identitystore#GroupMemberships``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.group_membership

GroupMemberships: TypeAlias = list[
    "capo_identitystore.types.group_membership.GroupMembership"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupMemberships) -> list:
    import capo_identitystore.types.group_membership

    out: list = []
    for item in value:
        out.append(
            capo_identitystore.types.group_membership.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupMemberships:
    import capo_identitystore.types.group_membership

    out: GroupMemberships = []
    for item in data:
        out.append(
            capo_identitystore.types.group_membership.deserialize_aws_json_1_1(item)
        )
    return out
