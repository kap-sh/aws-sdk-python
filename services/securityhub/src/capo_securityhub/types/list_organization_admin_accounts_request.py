"""Generated from Smithy shape ``com.amazonaws.securityhub#ListOrganizationAdminAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.admins_max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.security_hub_feature


class ListOrganizationAdminAccountsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_securityhub.types.admins_max_results.AdminsMaxResults"
    ]
    """<p>The maximum number of items to return in the response.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>ListOrganizationAdminAccounts</code> operation, set the value of this parameter to <code>NULL</code>. For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response. </p>"""
    feature: NotRequired[
        "capo_securityhub.types.security_hub_feature.SecurityHubFeature"
    ]
    """<p>The feature where the delegated administrator account is listed. Defaults to Security Hub CSPM if not specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationAdminAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOrganizationAdminAccountsRequest:
    out: ListOrganizationAdminAccountsRequest = {}  # type: ignore[typeddict-item]
    return out
