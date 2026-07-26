"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyReplicationInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_instance


class ModifyReplicationInstanceResponse(TypedDict, closed=True):
    replication_instance: NotRequired[
        "capo_database_migration_service.types.replication_instance.ReplicationInstance"
    ]
    """<p>The modified replication instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReplicationInstanceResponse) -> dict:
    out: dict = {}
    if "replication_instance" in value:
        import capo_database_migration_service.types.replication_instance

        out["ReplicationInstance"] = (
            capo_database_migration_service.types.replication_instance.serialize_aws_json_1_1(
                value["replication_instance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyReplicationInstanceResponse:
    out: ModifyReplicationInstanceResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationInstance" in data:
        import capo_database_migration_service.types.replication_instance

        out["replication_instance"] = (
            capo_database_migration_service.types.replication_instance.deserialize_aws_json_1_1(
                data["ReplicationInstance"]
            )
        )
    return out
