"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.subnet

SubnetList: TypeAlias = list["capo_database_migration_service.types.subnet.Subnet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetList) -> list:
    import capo_database_migration_service.types.subnet

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.subnet.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SubnetList:
    import capo_database_migration_service.types.subnet

    out: SubnetList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.subnet.deserialize_aws_json_1_1(item)
        )
    return out
