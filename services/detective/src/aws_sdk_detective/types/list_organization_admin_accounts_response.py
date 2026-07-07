"""Generated from Smithy shape ``com.amazonaws.detective#ListOrganizationAdminAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.administrator_list
    import aws_sdk_detective.types.pagination_token


class ListOrganizationAdminAccountsResponse(TypedDict, closed=True):
    administrators: NotRequired[
        "aws_sdk_detective.types.administrator_list.AdministratorList"
    ]
    """<p>The list of Detective administrator accounts.</p>"""
    next_token: NotRequired["aws_sdk_detective.types.pagination_token.PaginationToken"]
    """<p>If there are more accounts remaining in the results, then this is the pagination token to use to request the next page of accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationAdminAccountsResponse) -> dict:
    out: dict = {}
    if "administrators" in value:
        import aws_sdk_detective.types.administrator_list

        out["Administrators"] = (
            aws_sdk_detective.types.administrator_list.serialize_json(
                value["administrators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrganizationAdminAccountsResponse:
    out: ListOrganizationAdminAccountsResponse = {}  # type: ignore[typeddict-item]
    if "Administrators" in data:
        import aws_sdk_detective.types.administrator_list

        out["administrators"] = (
            aws_sdk_detective.types.administrator_list.deserialize_json(
                data["Administrators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
