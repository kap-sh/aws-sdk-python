"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReloadReplicationTablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class ReloadReplicationTablesResponse(TypedDict, closed=True):
    replication_config_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name of the replication config for which to reload tables.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReloadReplicationTablesResponse) -> dict:
    out: dict = {}
    if "replication_config_arn" in value:
        out["ReplicationConfigArn"] = value["replication_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReloadReplicationTablesResponse:
    out: ReloadReplicationTablesResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationConfigArn" in data:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    return out
