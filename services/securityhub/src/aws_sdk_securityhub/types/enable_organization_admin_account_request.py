"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.security_hub_feature


class EnableOrganizationAdminAccountRequest(TypedDict):
    admin_account_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account identifier of the account to designate as the Security Hub CSPM administrator account.</p>"""
    feature: NotRequired[
        "aws_sdk_securityhub.types.security_hub_feature.SecurityHubFeature"
    ]
    """<p>The feature for which the delegated admin account is enabled. Defaults to Security Hub CSPM if not specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["AdminAccountId"] = value["admin_account_id"]
    if "feature" in value:
        import aws_sdk_securityhub.types.security_hub_feature

        out["Feature"] = aws_sdk_securityhub.types.security_hub_feature.serialize_json(
            value["feature"]
        )
    return out


def deserialize_json(data: dict) -> EnableOrganizationAdminAccountRequest:
    out: EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "AdminAccountId" in data:
        out["admin_account_id"] = data["AdminAccountId"]
    if "Feature" in data:
        import aws_sdk_securityhub.types.security_hub_feature

        out["feature"] = (
            aws_sdk_securityhub.types.security_hub_feature.deserialize_json(
                data["Feature"]
            )
        )
    return out
