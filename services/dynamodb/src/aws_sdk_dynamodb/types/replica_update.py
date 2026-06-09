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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaUpdate) -> dict:
    out: dict = {}
    if "create" in value:
        import aws_sdk_dynamodb.types.create_replica_action

        out["Create"] = (
            aws_sdk_dynamodb.types.create_replica_action.serialize_aws_json_1_0(
                value["create"]
            )
        )
    if "delete" in value:
        import aws_sdk_dynamodb.types.delete_replica_action

        out["Delete"] = (
            aws_sdk_dynamodb.types.delete_replica_action.serialize_aws_json_1_0(
                value["delete"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaUpdate:
    out: ReplicaUpdate = {}  # type: ignore[typeddict-item]
    if "Create" in data:
        import aws_sdk_dynamodb.types.create_replica_action

        out["create"] = (
            aws_sdk_dynamodb.types.create_replica_action.deserialize_aws_json_1_0(
                data["Create"]
            )
        )
    if "Delete" in data:
        import aws_sdk_dynamodb.types.delete_replica_action

        out["delete"] = (
            aws_sdk_dynamodb.types.delete_replica_action.deserialize_aws_json_1_0(
                data["Delete"]
            )
        )
    return out
