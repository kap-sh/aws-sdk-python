"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.create_replica_action
    import aws_sdk_dynamodb.types.delete_replica_action


class ReplicaUpdate(TypedDict):
    create: NotRequired[
        "aws_sdk_dynamodb.types.create_replica_action.CreateReplicaAction"
    ]
    """<p>The parameters required for creating a replica on an existing global table.</p>"""
    delete: NotRequired[
        "aws_sdk_dynamodb.types.delete_replica_action.DeleteReplicaAction"
    ]
    """<p>The name of the existing replica to be removed.</p>"""
