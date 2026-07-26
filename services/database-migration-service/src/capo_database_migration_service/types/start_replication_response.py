"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication


class StartReplicationResponse(TypedDict, closed=True):
    replication: NotRequired[
        "capo_database_migration_service.types.replication.Replication"
    ]
    """<p>The replication that DMS started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationResponse) -> dict:
    out: dict = {}
    if "replication" in value:
        import capo_database_migration_service.types.replication

        out["Replication"] = (
            capo_database_migration_service.types.replication.serialize_aws_json_1_1(
                value["replication"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplicationResponse:
    out: StartReplicationResponse = {}  # type: ignore[typeddict-item]
    if "Replication" in data:
        import capo_database_migration_service.types.replication

        out["replication"] = (
            capo_database_migration_service.types.replication.deserialize_aws_json_1_1(
                data["Replication"]
            )
        )
    return out
