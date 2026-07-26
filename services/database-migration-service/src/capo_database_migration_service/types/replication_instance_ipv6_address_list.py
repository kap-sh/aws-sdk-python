"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationInstanceIpv6AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.string

ReplicationInstanceIpv6AddressList: TypeAlias = list[
    "capo_database_migration_service.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationInstanceIpv6AddressList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReplicationInstanceIpv6AddressList:
    return list(data)
