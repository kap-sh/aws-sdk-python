"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationInstancePublicIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.string

ReplicationInstancePublicIpAddressList: TypeAlias = list[
    "capo_database_migration_service.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationInstancePublicIpAddressList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReplicationInstancePublicIpAddressList:
    return list(data)
