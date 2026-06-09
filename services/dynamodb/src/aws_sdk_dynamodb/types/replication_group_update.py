"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicationGroupUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.create_replication_group_member_action
    import aws_sdk_dynamodb.types.delete_replication_group_member_action
    import aws_sdk_dynamodb.types.update_replication_group_member_action


class ReplicationGroupUpdate(TypedDict):
    create: NotRequired[
        "aws_sdk_dynamodb.types.create_replication_group_member_action.CreateReplicationGroupMemberAction"
    ]
    """<p>The parameters required for creating a replica for the table.</p>"""
    update: NotRequired[
        "aws_sdk_dynamodb.types.update_replication_group_member_action.UpdateReplicationGroupMemberAction"
    ]
    """<p>The parameters required for updating a replica for the table.</p>"""
    delete: NotRequired[
        "aws_sdk_dynamodb.types.delete_replication_group_member_action.DeleteReplicationGroupMemberAction"
    ]
    """<p>The parameters required for deleting a replica for the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationGroupUpdate) -> dict:
    out: dict = {}
    if "create" in value:
        import aws_sdk_dynamodb.types.create_replication_group_member_action

        out["Create"] = (
            aws_sdk_dynamodb.types.create_replication_group_member_action.serialize_aws_json_1_0(
                value["create"]
            )
        )
    if "update" in value:
        import aws_sdk_dynamodb.types.update_replication_group_member_action

        out["Update"] = (
            aws_sdk_dynamodb.types.update_replication_group_member_action.serialize_aws_json_1_0(
                value["update"]
            )
        )
    if "delete" in value:
        import aws_sdk_dynamodb.types.delete_replication_group_member_action

        out["Delete"] = (
            aws_sdk_dynamodb.types.delete_replication_group_member_action.serialize_aws_json_1_0(
                value["delete"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicationGroupUpdate:
    out: ReplicationGroupUpdate = {}  # type: ignore[typeddict-item]
    if "Create" in data:
        import aws_sdk_dynamodb.types.create_replication_group_member_action

        out["create"] = (
            aws_sdk_dynamodb.types.create_replication_group_member_action.deserialize_aws_json_1_0(
                data["Create"]
            )
        )
    if "Update" in data:
        import aws_sdk_dynamodb.types.update_replication_group_member_action

        out["update"] = (
            aws_sdk_dynamodb.types.update_replication_group_member_action.deserialize_aws_json_1_0(
                data["Update"]
            )
        )
    if "Delete" in data:
        import aws_sdk_dynamodb.types.delete_replication_group_member_action

        out["delete"] = (
            aws_sdk_dynamodb.types.delete_replication_group_member_action.deserialize_aws_json_1_0(
                data["Delete"]
            )
        )
    return out
