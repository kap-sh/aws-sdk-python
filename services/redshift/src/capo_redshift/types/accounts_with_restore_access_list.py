"""Generated from Smithy shape ``com.amazonaws.redshift#AccountsWithRestoreAccessList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.account_with_restore_access

AccountsWithRestoreAccessList: TypeAlias = list[
    "capo_redshift.types.account_with_restore_access.AccountWithRestoreAccess"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountsWithRestoreAccessList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.account_with_restore_access

    for n, item in enumerate(value, 1):
        capo_redshift.types.account_with_restore_access.serialize_query(
            item, pairs, f"{prefix}.AccountWithRestoreAccess.{n}"
        )


def deserialize_query(el: Element) -> AccountsWithRestoreAccessList:
    import capo_redshift.types.account_with_restore_access

    out: AccountsWithRestoreAccessList = []
    for child in el.findall("AccountWithRestoreAccess"):
        out.append(
            capo_redshift.types.account_with_restore_access.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AccountsWithRestoreAccessList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.account_with_restore_access

    for n, item in enumerate(value, 1):
        capo_redshift.types.account_with_restore_access.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AccountsWithRestoreAccessList:
    import capo_redshift.types.account_with_restore_access

    out: AccountsWithRestoreAccessList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.account_with_restore_access.deserialize_query(child)
        )
    return out
