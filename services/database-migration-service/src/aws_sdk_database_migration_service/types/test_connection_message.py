"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TestConnectionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class TestConnectionMessage(TypedDict, closed=True):
    replication_instance_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""
    endpoint_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestConnectionMessage) -> dict:
    out: dict = {}
    out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    out["EndpointArn"] = value["endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestConnectionMessage:
    out: TestConnectionMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    else:
        raise DeserializationError(
            "TestConnectionMessage.replication_instance_arn required"
        )
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    else:
        raise DeserializationError("TestConnectionMessage.endpoint_arn required")
    return out
