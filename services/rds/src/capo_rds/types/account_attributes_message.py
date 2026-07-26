"""Generated from Smithy shape ``com.amazonaws.rds#AccountAttributesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.account_quota_list


class AccountAttributesMessage(TypedDict, closed=True):
    account_quotas: NotRequired["capo_rds.types.account_quota_list.AccountQuotaList"]
    """<p>A list of <code>AccountQuota</code> objects. Within this list, each quota has a name, a count of usage toward the quota maximum, and a maximum value for the quota.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountAttributesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_quotas" in value:
        import capo_rds.types.account_quota_list

        capo_rds.types.account_quota_list.serialize_query(
            value["account_quotas"], pairs, f"{prefix}.AccountQuotas"
        )


def deserialize_query(el: Element) -> AccountAttributesMessage:
    out: AccountAttributesMessage = {}  # type: ignore[typeddict-item]
    child_account_quotas = el.find("AccountQuotas")
    if child_account_quotas is not None:
        import capo_rds.types.account_quota_list

        out["account_quotas"] = capo_rds.types.account_quota_list.deserialize_query(
            child_account_quotas
        )
    return out
