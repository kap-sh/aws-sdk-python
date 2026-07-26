"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicationGroupUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.create_replication_group_member_action
    import capo_dynamodb.types.delete_replication_group_member_action
    import capo_dynamodb.types.update_replication_group_member_action


class ReplicationGroupUpdate(TypedDict, closed=True):
    create: NotRequired[
        "capo_dynamodb.types.create_replication_group_member_action.CreateReplicationGroupMemberAction"
    ]
    """<p>The parameters required for creating a replica for the table.</p>"""
    update: NotRequired[
        "capo_dynamodb.types.update_replication_group_member_action.UpdateReplicationGroupMemberAction"
    ]
    """<p>The parameters required for updating a replica for the table.</p>"""
    delete: NotRequired[
        "capo_dynamodb.types.delete_replication_group_member_action.DeleteReplicationGroupMemberAction"
    ]
    """<p>The parameters required for deleting a replica for the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationGroupUpdate) -> dict:
    out: dict = {}
    if "create" in value:
        import capo_dynamodb.types.create_replication_group_member_action

        out["Create"] = (
            capo_dynamodb.types.create_replication_group_member_action.serialize_aws_json_1_0(
                value["create"]
            )
        )
    if "update" in value:
        import capo_dynamodb.types.update_replication_group_member_action

        out["Update"] = (
            capo_dynamodb.types.update_replication_group_member_action.serialize_aws_json_1_0(
                value["update"]
            )
        )
    if "delete" in value:
        import capo_dynamodb.types.delete_replication_group_member_action

        out["Delete"] = (
            capo_dynamodb.types.delete_replication_group_member_action.serialize_aws_json_1_0(
                value["delete"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicationGroupUpdate:
    out: ReplicationGroupUpdate = {}  # type: ignore[typeddict-item]
    if "Create" in data:
        import capo_dynamodb.types.create_replication_group_member_action

        out["create"] = (
            capo_dynamodb.types.create_replication_group_member_action.deserialize_aws_json_1_0(
                data["Create"]
            )
        )
    if "Update" in data:
        import capo_dynamodb.types.update_replication_group_member_action

        out["update"] = (
            capo_dynamodb.types.update_replication_group_member_action.deserialize_aws_json_1_0(
                data["Update"]
            )
        )
    if "Delete" in data:
        import capo_dynamodb.types.delete_replication_group_member_action

        out["delete"] = (
            capo_dynamodb.types.delete_replication_group_member_action.deserialize_aws_json_1_0(
                data["Delete"]
            )
        )
    return out
