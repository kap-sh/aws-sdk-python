"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateReplicationConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_config


class CreateReplicationConfigResponse(TypedDict):
    replication_config: NotRequired[
        "aws_sdk_database_migration_service.types.replication_config.ReplicationConfig"
    ]
    """<p>Configuration parameters returned from the DMS Serverless replication after it is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReplicationConfigResponse) -> dict:
    out: dict = {}
    if "replication_config" in value:
        import aws_sdk_database_migration_service.types.replication_config

        out["ReplicationConfig"] = (
            aws_sdk_database_migration_service.types.replication_config.serialize_aws_json_1_1(
                value["replication_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReplicationConfigResponse:
    out: CreateReplicationConfigResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationConfig" in data:
        import aws_sdk_database_migration_service.types.replication_config

        out["replication_config"] = (
            aws_sdk_database_migration_service.types.replication_config.deserialize_aws_json_1_1(
                data["ReplicationConfig"]
            )
        )
    return out
