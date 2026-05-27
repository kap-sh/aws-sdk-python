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
