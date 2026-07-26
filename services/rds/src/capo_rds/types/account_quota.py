"""Generated from Smithy shape ``com.amazonaws.rds#AccountQuota``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.long
    import capo_rds.types.string


class AccountQuota(TypedDict, closed=True):
    account_quota_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the Amazon RDS quota for this Amazon Web Services account.</p>"""
    used: NotRequired["capo_rds.types.long.Long"]
    """<p>The amount currently used toward the quota maximum.</p>"""
    max: NotRequired["capo_rds.types.long.Long"]
    """<p>The maximum allowed value for the quota.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountQuota, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_quota_name" in value:
        pairs.append((f"{prefix}.AccountQuotaName", str(value["account_quota_name"])))
    if "used" in value:
        pairs.append((f"{prefix}.Used", str(value["used"])))
    if "max" in value:
        pairs.append((f"{prefix}.Max", str(value["max"])))


def deserialize_query(el: Element) -> AccountQuota:
    out: AccountQuota = {}  # type: ignore[typeddict-item]
    child_account_quota_name = el.find("AccountQuotaName")
    if child_account_quota_name is not None:
        out["account_quota_name"] = str(child_account_quota_name.text or "")
    child_used = el.find("Used")
    if child_used is not None:
        out["used"] = int(child_used.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = int(child_max.text or "")
    return out
