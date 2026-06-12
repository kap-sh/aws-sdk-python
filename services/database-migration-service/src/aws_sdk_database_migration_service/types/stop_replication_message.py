"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StopReplicationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class StopReplicationMessage(TypedDict):
    replication_config_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name of the replication to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigArn"] = value["replication_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationMessage:
    out: StopReplicationMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationConfigArn" in data:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    else:
        raise DeserializationError(
            "StopReplicationMessage.replication_config_arn required"
        )
    return out
