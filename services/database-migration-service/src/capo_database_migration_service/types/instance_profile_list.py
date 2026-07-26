"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#InstanceProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.instance_profile

InstanceProfileList: TypeAlias = list[
    "capo_database_migration_service.types.instance_profile.InstanceProfile"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceProfileList) -> list:
    import capo_database_migration_service.types.instance_profile

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.instance_profile.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceProfileList:
    import capo_database_migration_service.types.instance_profile

    out: InstanceProfileList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.instance_profile.deserialize_aws_json_1_1(
                item
            )
        )
    return out
