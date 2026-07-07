"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteConnectionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DeleteConnectionMessage(TypedDict, closed=True):
    endpoint_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>"""
    replication_instance_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionMessage) -> dict:
    out: dict = {}
    out["EndpointArn"] = value["endpoint_arn"]
    out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectionMessage:
    out: DeleteConnectionMessage = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    else:
        raise DeserializationError("DeleteConnectionMessage.endpoint_arn required")
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    else:
        raise DeserializationError(
            "DeleteConnectionMessage.replication_instance_arn required"
        )
    return out
