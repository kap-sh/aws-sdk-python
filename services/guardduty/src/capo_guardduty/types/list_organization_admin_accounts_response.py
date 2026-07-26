"""Generated from Smithy shape ``com.amazonaws.guardduty#ListOrganizationAdminAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.admin_accounts
    import capo_guardduty.types.string


class ListOrganizationAdminAccountsResponse(TypedDict, closed=True):
    admin_accounts: NotRequired["capo_guardduty.types.admin_accounts.AdminAccounts"]
    """<p>A list of accounts configured as GuardDuty delegated administrators.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationAdminAccountsResponse) -> dict:
    out: dict = {}
    if "admin_accounts" in value:
        import capo_guardduty.types.admin_accounts

        out["adminAccounts"] = capo_guardduty.types.admin_accounts.serialize_json(
            value["admin_accounts"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrganizationAdminAccountsResponse:
    out: ListOrganizationAdminAccountsResponse = {}  # type: ignore[typeddict-item]
    if "adminAccounts" in data:
        import capo_guardduty.types.admin_accounts

        out["admin_accounts"] = capo_guardduty.types.admin_accounts.deserialize_json(
            data["adminAccounts"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
