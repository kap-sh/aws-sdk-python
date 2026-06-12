"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountsForProvisionedPermissionSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.account_list
    import aws_sdk_sso_admin.types.token


class ListAccountsForProvisionedPermissionSetResponse(TypedDict):
    account_ids: NotRequired["aws_sdk_sso_admin.types.account_list.AccountList"]
    """<p>The list of Amazon Web Services <code>AccountIds</code>.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListAccountsForProvisionedPermissionSetResponse,
) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_sso_admin.types.account_list

        out["AccountIds"] = aws_sdk_sso_admin.types.account_list.serialize_aws_json_1_1(
            value["account_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListAccountsForProvisionedPermissionSetResponse:
    out: ListAccountsForProvisionedPermissionSetResponse = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_sso_admin.types.account_list

        out["account_ids"] = (
            aws_sdk_sso_admin.types.account_list.deserialize_aws_json_1_1(
                data["AccountIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
