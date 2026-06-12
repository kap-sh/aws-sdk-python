"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AccountQuotaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.account_quota

AccountQuotaList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.account_quota.AccountQuota"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountQuotaList) -> list:
    import aws_sdk_database_migration_service.types.account_quota

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.account_quota.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountQuotaList:
    import aws_sdk_database_migration_service.types.account_quota

    out: AccountQuotaList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.account_quota.deserialize_aws_json_1_1(
                item
            )
        )
    return out
