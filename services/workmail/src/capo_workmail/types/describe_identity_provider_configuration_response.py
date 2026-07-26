"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeIdentityProviderConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.identity_center_configuration
    import capo_workmail.types.identity_provider_authentication_mode
    import capo_workmail.types.personal_access_token_configuration


class DescribeIdentityProviderConfigurationResponse(TypedDict, closed=True):
    authentication_mode: NotRequired[
        "capo_workmail.types.identity_provider_authentication_mode.IdentityProviderAuthenticationMode"
    ]
    """<p> The authentication mode used in WorkMail.</p>"""
    identity_center_configuration: NotRequired[
        "capo_workmail.types.identity_center_configuration.IdentityCenterConfiguration"
    ]
    """<p> The details of the IAM Identity Center configuration. </p>"""
    personal_access_token_configuration: NotRequired[
        "capo_workmail.types.personal_access_token_configuration.PersonalAccessTokenConfiguration"
    ]
    """<p> The details of the Personal Access Token configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeIdentityProviderConfigurationResponse,
) -> dict:
    out: dict = {}
    if "authentication_mode" in value:
        import capo_workmail.types.identity_provider_authentication_mode

        out["AuthenticationMode"] = (
            capo_workmail.types.identity_provider_authentication_mode.serialize_aws_json_1_1(
                value["authentication_mode"]
            )
        )
    if "identity_center_configuration" in value:
        import capo_workmail.types.identity_center_configuration

        out["IdentityCenterConfiguration"] = (
            capo_workmail.types.identity_center_configuration.serialize_aws_json_1_1(
                value["identity_center_configuration"]
            )
        )
    if "personal_access_token_configuration" in value:
        import capo_workmail.types.personal_access_token_configuration

        out["PersonalAccessTokenConfiguration"] = (
            capo_workmail.types.personal_access_token_configuration.serialize_aws_json_1_1(
                value["personal_access_token_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeIdentityProviderConfigurationResponse:
    out: DescribeIdentityProviderConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationMode" in data:
        import capo_workmail.types.identity_provider_authentication_mode

        out["authentication_mode"] = (
            capo_workmail.types.identity_provider_authentication_mode.deserialize_aws_json_1_1(
                data["AuthenticationMode"]
            )
        )
    if "IdentityCenterConfiguration" in data:
        import capo_workmail.types.identity_center_configuration

        out["identity_center_configuration"] = (
            capo_workmail.types.identity_center_configuration.deserialize_aws_json_1_1(
                data["IdentityCenterConfiguration"]
            )
        )
    if "PersonalAccessTokenConfiguration" in data:
        import capo_workmail.types.personal_access_token_configuration

        out["personal_access_token_configuration"] = (
            capo_workmail.types.personal_access_token_configuration.deserialize_aws_json_1_1(
                data["PersonalAccessTokenConfiguration"]
            )
        )
    return out
