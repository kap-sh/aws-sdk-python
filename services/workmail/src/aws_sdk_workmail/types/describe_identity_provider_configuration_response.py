"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeIdentityProviderConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.identity_center_configuration
    import aws_sdk_workmail.types.identity_provider_authentication_mode
    import aws_sdk_workmail.types.personal_access_token_configuration


class DescribeIdentityProviderConfigurationResponse(TypedDict):
    authentication_mode: NotRequired[
        "aws_sdk_workmail.types.identity_provider_authentication_mode.IdentityProviderAuthenticationMode"
    ]
    """<p> The authentication mode used in WorkMail.</p>"""
    identity_center_configuration: NotRequired[
        "aws_sdk_workmail.types.identity_center_configuration.IdentityCenterConfiguration"
    ]
    """<p> The details of the IAM Identity Center configuration. </p>"""
    personal_access_token_configuration: NotRequired[
        "aws_sdk_workmail.types.personal_access_token_configuration.PersonalAccessTokenConfiguration"
    ]
    """<p> The details of the Personal Access Token configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeIdentityProviderConfigurationResponse,
) -> dict:
    out: dict = {}
    if "authentication_mode" in value:
        import aws_sdk_workmail.types.identity_provider_authentication_mode

        out["AuthenticationMode"] = (
            aws_sdk_workmail.types.identity_provider_authentication_mode.serialize_aws_json_1_1(
                value["authentication_mode"]
            )
        )
    if "identity_center_configuration" in value:
        import aws_sdk_workmail.types.identity_center_configuration

        out["IdentityCenterConfiguration"] = (
            aws_sdk_workmail.types.identity_center_configuration.serialize_aws_json_1_1(
                value["identity_center_configuration"]
            )
        )
    if "personal_access_token_configuration" in value:
        import aws_sdk_workmail.types.personal_access_token_configuration

        out["PersonalAccessTokenConfiguration"] = (
            aws_sdk_workmail.types.personal_access_token_configuration.serialize_aws_json_1_1(
                value["personal_access_token_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeIdentityProviderConfigurationResponse:
    out: DescribeIdentityProviderConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationMode" in data:
        import aws_sdk_workmail.types.identity_provider_authentication_mode

        out["authentication_mode"] = (
            aws_sdk_workmail.types.identity_provider_authentication_mode.deserialize_aws_json_1_1(
                data["AuthenticationMode"]
            )
        )
    if "IdentityCenterConfiguration" in data:
        import aws_sdk_workmail.types.identity_center_configuration

        out["identity_center_configuration"] = (
            aws_sdk_workmail.types.identity_center_configuration.deserialize_aws_json_1_1(
                data["IdentityCenterConfiguration"]
            )
        )
    if "PersonalAccessTokenConfiguration" in data:
        import aws_sdk_workmail.types.personal_access_token_configuration

        out["personal_access_token_configuration"] = (
            aws_sdk_workmail.types.personal_access_token_configuration.deserialize_aws_json_1_1(
                data["PersonalAccessTokenConfiguration"]
            )
        )
    return out
