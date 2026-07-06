"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteReplicationConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_config


class DeleteReplicationConfigResponse(TypedDict, closed=True):
    replication_config: NotRequired[
        "aws_sdk_database_migration_service.types.replication_config.ReplicationConfig"
    ]
    """<p>Configuration parameters returned for the DMS Serverless replication after it is deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplicationConfigResponse) -> dict:
    out: dict = {}
    if "replication_config" in value:
        import aws_sdk_database_migration_service.types.replication_config

        out["ReplicationConfig"] = (
            aws_sdk_database_migration_service.types.replication_config.serialize_aws_json_1_1(
                value["replication_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplicationConfigResponse:
    out: DeleteReplicationConfigResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationConfig" in data:
        import aws_sdk_database_migration_service.types.replication_config

        out["replication_config"] = (
            aws_sdk_database_migration_service.types.replication_config.deserialize_aws_json_1_1(
                data["ReplicationConfig"]
            )
        )
    return out
