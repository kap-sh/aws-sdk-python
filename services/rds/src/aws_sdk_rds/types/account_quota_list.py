"""Generated from Smithy shape ``com.amazonaws.rds#AccountQuotaList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.account_quota

AccountQuotaList: TypeAlias = list["aws_sdk_rds.types.account_quota.AccountQuota"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountQuotaList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.account_quota

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.account_quota.serialize_query(
            item, pairs, f"{prefix}.AccountQuota.{n}"
        )


def deserialize_query(el: Element) -> AccountQuotaList:
    import aws_sdk_rds.types.account_quota

    out: AccountQuotaList = []
    for child in el.findall("AccountQuota"):
        out.append(aws_sdk_rds.types.account_quota.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AccountQuotaList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.account_quota

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.account_quota.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> AccountQuotaList:
    import aws_sdk_rds.types.account_quota

    out: AccountQuotaList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.account_quota.deserialize_query(child))
    return out
