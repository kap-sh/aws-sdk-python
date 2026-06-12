"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateReplicationInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_instance


class CreateReplicationInstanceResponse(TypedDict):
    replication_instance: NotRequired[
        "aws_sdk_database_migration_service.types.replication_instance.ReplicationInstance"
    ]
    """<p>The replication instance that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReplicationInstanceResponse) -> dict:
    out: dict = {}
    if "replication_instance" in value:
        import aws_sdk_database_migration_service.types.replication_instance

        out["ReplicationInstance"] = (
            aws_sdk_database_migration_service.types.replication_instance.serialize_aws_json_1_1(
                value["replication_instance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReplicationInstanceResponse:
    out: CreateReplicationInstanceResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationInstance" in data:
        import aws_sdk_database_migration_service.types.replication_instance

        out["replication_instance"] = (
            aws_sdk_database_migration_service.types.replication_instance.deserialize_aws_json_1_1(
                data["ReplicationInstance"]
            )
        )
    return out
