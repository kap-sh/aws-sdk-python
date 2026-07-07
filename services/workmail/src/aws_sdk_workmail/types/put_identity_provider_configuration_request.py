"""Generated from Smithy shape ``com.amazonaws.workmail#PutIdentityProviderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.identity_center_configuration
    import aws_sdk_workmail.types.identity_provider_authentication_mode
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.personal_access_token_configuration


class PutIdentityProviderConfigurationRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p> The ID of the WorkMail Organization. </p>"""
    authentication_mode: "aws_sdk_workmail.types.identity_provider_authentication_mode.IdentityProviderAuthenticationMode"
    """<p> The authentication mode used in WorkMail.</p>"""
    identity_center_configuration: "aws_sdk_workmail.types.identity_center_configuration.IdentityCenterConfiguration"
    """<p> The details of the IAM Identity Center configuration.</p>"""
    personal_access_token_configuration: "aws_sdk_workmail.types.personal_access_token_configuration.PersonalAccessTokenConfiguration"
    """<p> The details of the Personal Access Token configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutIdentityProviderConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    import aws_sdk_workmail.types.identity_provider_authentication_mode

    out["AuthenticationMode"] = (
        aws_sdk_workmail.types.identity_provider_authentication_mode.serialize_aws_json_1_1(
            value["authentication_mode"]
        )
    )
    import aws_sdk_workmail.types.identity_center_configuration

    out["IdentityCenterConfiguration"] = (
        aws_sdk_workmail.types.identity_center_configuration.serialize_aws_json_1_1(
            value["identity_center_configuration"]
        )
    )
    import aws_sdk_workmail.types.personal_access_token_configuration

    out["PersonalAccessTokenConfiguration"] = (
        aws_sdk_workmail.types.personal_access_token_configuration.serialize_aws_json_1_1(
            value["personal_access_token_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutIdentityProviderConfigurationRequest:
    out: PutIdentityProviderConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "PutIdentityProviderConfigurationRequest.organization_id required"
        )
    if "AuthenticationMode" in data:
        import aws_sdk_workmail.types.identity_provider_authentication_mode

        out["authentication_mode"] = (
            aws_sdk_workmail.types.identity_provider_authentication_mode.deserialize_aws_json_1_1(
                data["AuthenticationMode"]
            )
        )
    else:
        raise DeserializationError(
            "PutIdentityProviderConfigurationRequest.authentication_mode required"
        )
    if "IdentityCenterConfiguration" in data:
        import aws_sdk_workmail.types.identity_center_configuration

        out["identity_center_configuration"] = (
            aws_sdk_workmail.types.identity_center_configuration.deserialize_aws_json_1_1(
                data["IdentityCenterConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutIdentityProviderConfigurationRequest.identity_center_configuration required"
        )
    if "PersonalAccessTokenConfiguration" in data:
        import aws_sdk_workmail.types.personal_access_token_configuration

        out["personal_access_token_configuration"] = (
            aws_sdk_workmail.types.personal_access_token_configuration.deserialize_aws_json_1_1(
                data["PersonalAccessTokenConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutIdentityProviderConfigurationRequest.personal_access_token_configuration required"
        )
    return out
