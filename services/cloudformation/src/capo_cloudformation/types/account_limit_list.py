"""Generated from Smithy shape ``com.amazonaws.cloudformation#AccountLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account_limit

AccountLimitList: TypeAlias = list[
    "capo_cloudformation.types.account_limit.AccountLimit"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountLimitList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.account_limit

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.account_limit.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AccountLimitList:
    import capo_cloudformation.types.account_limit

    out: AccountLimitList = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.account_limit.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AccountLimitList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.account_limit

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.account_limit.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AccountLimitList:
    import capo_cloudformation.types.account_limit

    out: AccountLimitList = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.account_limit.deserialize_query(child))
    return out
