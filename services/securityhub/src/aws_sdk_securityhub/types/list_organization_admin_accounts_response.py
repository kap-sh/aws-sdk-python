"""Generated from Smithy shape ``com.amazonaws.securityhub#ListOrganizationAdminAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.admin_accounts
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.security_hub_feature


class ListOrganizationAdminAccountsResponse(TypedDict):
    admin_accounts: NotRequired[
        "aws_sdk_securityhub.types.admin_accounts.AdminAccounts"
    ]
    """<p>The list of Security Hub CSPM administrator accounts.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""
    feature: NotRequired[
        "aws_sdk_securityhub.types.security_hub_feature.SecurityHubFeature"
    ]
    """<p>The feature where the delegated administrator account is listed. Defaults to Security Hub CSPM CSPM if not specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationAdminAccountsResponse) -> dict:
    out: dict = {}
    if "admin_accounts" in value:
        import aws_sdk_securityhub.types.admin_accounts

        out["AdminAccounts"] = aws_sdk_securityhub.types.admin_accounts.serialize_json(
            value["admin_accounts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "feature" in value:
        import aws_sdk_securityhub.types.security_hub_feature

        out["Feature"] = aws_sdk_securityhub.types.security_hub_feature.serialize_json(
            value["feature"]
        )
    return out


def deserialize_json(data: dict) -> ListOrganizationAdminAccountsResponse:
    out: ListOrganizationAdminAccountsResponse = {}  # type: ignore[typeddict-item]
    if "AdminAccounts" in data:
        import aws_sdk_securityhub.types.admin_accounts

        out["admin_accounts"] = (
            aws_sdk_securityhub.types.admin_accounts.deserialize_json(
                data["AdminAccounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Feature" in data:
        import aws_sdk_securityhub.types.security_hub_feature

        out["feature"] = (
            aws_sdk_securityhub.types.security_hub_feature.deserialize_json(
                data["Feature"]
            )
        )
    return out
