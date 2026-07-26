"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.security_hub_feature


class EnableOrganizationAdminAccountRequest(TypedDict, closed=True):
    admin_account_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account identifier of the account to designate as the Security Hub CSPM administrator account.</p>"""
    feature: NotRequired[
        "capo_securityhub.types.security_hub_feature.SecurityHubFeature"
    ]
    """<p>The feature for which the delegated admin account is enabled. Defaults to Security Hub CSPM if not specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["AdminAccountId"] = value["admin_account_id"]
    if "feature" in value:
        import capo_securityhub.types.security_hub_feature

        out["Feature"] = capo_securityhub.types.security_hub_feature.serialize_json(
            value["feature"]
        )
    return out


def deserialize_json(data: dict) -> EnableOrganizationAdminAccountRequest:
    out: EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "AdminAccountId" in data:
        out["admin_account_id"] = data["AdminAccountId"]
    if "Feature" in data:
        import capo_securityhub.types.security_hub_feature

        out["feature"] = capo_securityhub.types.security_hub_feature.deserialize_json(
            data["Feature"]
        )
    return out
