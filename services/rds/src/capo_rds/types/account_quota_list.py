"""Generated from Smithy shape ``com.amazonaws.rds#AccountQuotaList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.account_quota

AccountQuotaList: TypeAlias = list["capo_rds.types.account_quota.AccountQuota"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountQuotaList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.account_quota

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.account_quota.serialize_query(
            item, pairs, f"{prefix}.AccountQuota.{n}"
        )


def deserialize_query(el: Element) -> AccountQuotaList:
    import capo_rds.types.account_quota

    out: AccountQuotaList = []
    for child in el.findall("AccountQuota"):
        out.append(capo_rds.types.account_quota.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AccountQuotaList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.account_quota

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.account_quota.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> AccountQuotaList:
    import capo_rds.types.account_quota

    out: AccountQuotaList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.account_quota.deserialize_query(child))
    return out
