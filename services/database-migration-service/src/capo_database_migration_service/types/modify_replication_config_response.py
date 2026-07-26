"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyReplicationConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_config


class ModifyReplicationConfigResponse(TypedDict, closed=True):
    replication_config: NotRequired[
        "capo_database_migration_service.types.replication_config.ReplicationConfig"
    ]
    """<p>Information about the serverless replication config that was modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReplicationConfigResponse) -> dict:
    out: dict = {}
    if "replication_config" in value:
        import capo_database_migration_service.types.replication_config

        out["ReplicationConfig"] = (
            capo_database_migration_service.types.replication_config.serialize_aws_json_1_1(
                value["replication_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyReplicationConfigResponse:
    out: ModifyReplicationConfigResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationConfig" in data:
        import capo_database_migration_service.types.replication_config

        out["replication_config"] = (
            capo_database_migration_service.types.replication_config.deserialize_aws_json_1_1(
                data["ReplicationConfig"]
            )
        )
    return out
