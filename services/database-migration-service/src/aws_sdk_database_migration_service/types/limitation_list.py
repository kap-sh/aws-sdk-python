"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#LimitationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.limitation

LimitationList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.limitation.Limitation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitationList) -> list:
    import aws_sdk_database_migration_service.types.limitation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.limitation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LimitationList:
    import aws_sdk_database_migration_service.types.limitation

    out: LimitationList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.limitation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
