"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateReplicationSubnetGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_subnet_group


class CreateReplicationSubnetGroupResponse(TypedDict):
    replication_subnet_group: NotRequired[
        "aws_sdk_database_migration_service.types.replication_subnet_group.ReplicationSubnetGroup"
    ]
    """<p>The replication subnet group that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReplicationSubnetGroupResponse) -> dict:
    out: dict = {}
    if "replication_subnet_group" in value:
        import aws_sdk_database_migration_service.types.replication_subnet_group

        out["ReplicationSubnetGroup"] = (
            aws_sdk_database_migration_service.types.replication_subnet_group.serialize_aws_json_1_1(
                value["replication_subnet_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReplicationSubnetGroupResponse:
    out: CreateReplicationSubnetGroupResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationSubnetGroup" in data:
        import aws_sdk_database_migration_service.types.replication_subnet_group

        out["replication_subnet_group"] = (
            aws_sdk_database_migration_service.types.replication_subnet_group.deserialize_aws_json_1_1(
                data["ReplicationSubnetGroup"]
            )
        )
    return out
