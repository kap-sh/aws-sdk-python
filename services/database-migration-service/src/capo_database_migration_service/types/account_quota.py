"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AccountQuota``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.long
    import capo_database_migration_service.types.string


class AccountQuota(TypedDict, closed=True):
    account_quota_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The name of the DMS quota for this Amazon Web Services account.</p>"""
    used: "capo_database_migration_service.types.long.Long"
    """<p>The amount currently used toward the quota maximum.</p>"""
    max: "capo_database_migration_service.types.long.Long"
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
