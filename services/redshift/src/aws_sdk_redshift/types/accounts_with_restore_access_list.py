"""Generated from Smithy shape ``com.amazonaws.redshift#AccountsWithRestoreAccessList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.account_with_restore_access

AccountsWithRestoreAccessList: TypeAlias = list[
    "aws_sdk_redshift.types.account_with_restore_access.AccountWithRestoreAccess"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountsWithRestoreAccessList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.account_with_restore_access

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.account_with_restore_access.serialize_query(
            item, pairs, f"{prefix}.AccountWithRestoreAccess.{n}"
        )


def deserialize_query(el: Element) -> AccountsWithRestoreAccessList:
    import aws_sdk_redshift.types.account_with_restore_access

    out: AccountsWithRestoreAccessList = []
    for child in el.findall("AccountWithRestoreAccess"):
        out.append(
            aws_sdk_redshift.types.account_with_restore_access.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AccountsWithRestoreAccessList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.account_with_restore_access

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.account_with_restore_access.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AccountsWithRestoreAccessList:
    import aws_sdk_redshift.types.account_with_restore_access

    out: AccountsWithRestoreAccessList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.account_with_restore_access.deserialize_query(child)
        )
    return out
