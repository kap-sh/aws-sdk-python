"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteReplicationSubnetGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DeleteReplicationSubnetGroupMessage(TypedDict):
    replication_subnet_group_identifier: (
        "aws_sdk_database_migration_service.types.string.String"
    )
    """<p>The subnet group name of the replication instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplicationSubnetGroupMessage) -> dict:
    out: dict = {}
    out["ReplicationSubnetGroupIdentifier"] = value[
        "replication_subnet_group_identifier"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplicationSubnetGroupMessage:
    out: DeleteReplicationSubnetGroupMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationSubnetGroupIdentifier" in data:
        out["replication_subnet_group_identifier"] = data[
            "ReplicationSubnetGroupIdentifier"
        ]
    else:
        raise DeserializationError(
            "DeleteReplicationSubnetGroupMessage.replication_subnet_group_identifier required"
        )
    return out
