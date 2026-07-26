"""Generated from Smithy shape ``com.amazonaws.identitystore#GroupMembershipExistenceResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.group_membership_existence_result

GroupMembershipExistenceResults: TypeAlias = list[
    "capo_identitystore.types.group_membership_existence_result.GroupMembershipExistenceResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupMembershipExistenceResults) -> list:
    import capo_identitystore.types.group_membership_existence_result

    out: list = []
    for item in value:
        out.append(
            capo_identitystore.types.group_membership_existence_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupMembershipExistenceResults:
    import capo_identitystore.types.group_membership_existence_result

    out: GroupMembershipExistenceResults = []
    for item in data:
        out.append(
            capo_identitystore.types.group_membership_existence_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
