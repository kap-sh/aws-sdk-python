"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StopReplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication


class StopReplicationResponse(TypedDict):
    replication: NotRequired[
        "aws_sdk_database_migration_service.types.replication.Replication"
    ]
    """<p>The replication that DMS stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationResponse) -> dict:
    out: dict = {}
    if "replication" in value:
        import aws_sdk_database_migration_service.types.replication

        out["Replication"] = (
            aws_sdk_database_migration_service.types.replication.serialize_aws_json_1_1(
                value["replication"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationResponse:
    out: StopReplicationResponse = {}  # type: ignore[typeddict-item]
    if "Replication" in data:
        import aws_sdk_database_migration_service.types.replication

        out["replication"] = (
            aws_sdk_database_migration_service.types.replication.deserialize_aws_json_1_1(
                data["Replication"]
            )
        )
    return out
