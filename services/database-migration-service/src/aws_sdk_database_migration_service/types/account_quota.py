"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AccountQuota``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.long
    import aws_sdk_database_migration_service.types.string


class AccountQuota(TypedDict):
    account_quota_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name of the DMS quota for this Amazon Web Services account.</p>"""
    used: "aws_sdk_database_migration_service.types.long.Long"
    """<p>The amount currently used toward the quota maximum.</p>"""
    max: "aws_sdk_database_migration_service.types.long.Long"
    """<p>The maximum allowed value for the quota.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountQuota) -> dict:
    out: dict = {}
    if "account_quota_name" in value:
        out["AccountQuotaName"] = value["account_quota_name"]
    out["Used"] = value.get("used", 0)
    out["Max"] = value.get("max", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountQuota:
    out: AccountQuota = {}  # type: ignore[typeddict-item]
    if "AccountQuotaName" in data:
        out["account_quota_name"] = data["AccountQuotaName"]
    if "Used" in data:
        out["used"] = data["Used"]
    else:
        out["used"] = 0
    if "Max" in data:
        out["max"] = data["Max"]
    else:
        out["max"] = 0
    return out
