"""Generated from Smithy shape ``com.amazonaws.macie2#ListOrganizationAdminAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_admin_account
    import aws_sdk_macie2.types.__string


class ListOrganizationAdminAccountsResponse(TypedDict, closed=True):
    admin_accounts: NotRequired[
        "aws_sdk_macie2.types.__list_of_admin_account.__listOfAdminAccount"
    ]
    """<p>An array of objects, one for each delegated Amazon Macie administrator account for the organization. Only one of these accounts can have a status of ENABLED.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationAdminAccountsResponse) -> dict:
    out: dict = {}
    if "admin_accounts" in value:
        import aws_sdk_macie2.types.__list_of_admin_account

        out["adminAccounts"] = (
            aws_sdk_macie2.types.__list_of_admin_account.serialize_json(
                value["admin_accounts"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrganizationAdminAccountsResponse:
    out: ListOrganizationAdminAccountsResponse = {}  # type: ignore[typeddict-item]
    if "adminAccounts" in data:
        import aws_sdk_macie2.types.__list_of_admin_account

        out["admin_accounts"] = (
            aws_sdk_macie2.types.__list_of_admin_account.deserialize_json(
                data["adminAccounts"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
