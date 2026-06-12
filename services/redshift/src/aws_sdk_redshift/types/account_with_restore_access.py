"""Generated from Smithy shape ``com.amazonaws.redshift#AccountWithRestoreAccess``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class AccountWithRestoreAccess(TypedDict):
    account_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of an Amazon Web Services account authorized to restore a snapshot.</p>"""
    account_alias: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of an Amazon Web Services support account authorized to restore a snapshot. For Amazon Web Services Support, the identifier is <code>amazon-redshift-support</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountWithRestoreAccess, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_id" in value:
        pairs.append((f"{prefix}.AccountId", str(value["account_id"])))
    if "account_alias" in value:
        pairs.append((f"{prefix}.AccountAlias", str(value["account_alias"])))


def deserialize_query(el: Element) -> AccountWithRestoreAccess:
    out: AccountWithRestoreAccess = {}  # type: ignore[typeddict-item]
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_account_alias = el.find("AccountAlias")
    if child_account_alias is not None:
        out["account_alias"] = str(child_account_alias.text or "")
    return out
