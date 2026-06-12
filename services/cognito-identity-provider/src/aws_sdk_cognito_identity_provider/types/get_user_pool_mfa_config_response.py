"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUserPoolMfaConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.email_mfa_config_type
    import aws_sdk_cognito_identity_provider.types.sms_mfa_config_type
    import aws_sdk_cognito_identity_provider.types.software_token_mfa_config_type
    import aws_sdk_cognito_identity_provider.types.user_pool_mfa_type
    import aws_sdk_cognito_identity_provider.types.web_authn_configuration_type


class GetUserPoolMfaConfigResponse(TypedDict):
    sms_mfa_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.sms_mfa_config_type.SmsMfaConfigType"
    ]
    """<p>Shows user pool configuration for SMS message MFA. Includes the message template and the SMS message sending configuration for Amazon SNS.</p>"""
    software_token_mfa_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.software_token_mfa_config_type.SoftwareTokenMfaConfigType"
    ]
    """<p>Shows user pool configuration for time-based one-time password (TOTP) MFA. Includes TOTP enabled or disabled state.</p>"""
    email_mfa_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.email_mfa_config_type.EmailMfaConfigType"
    ]
    """<p>Shows configuration for user pool email message MFA and sign-in with one-time passwords (OTPs). Includes the subject and body of the email message template for sign-in and MFA messages. To activate this setting, your user pool must be in the <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html\"> Essentials tier</a> or higher.</p>"""
    mfa_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_mfa_type.UserPoolMfaType"
    ]
    """<p>Displays the state of multi-factor authentication (MFA) as on, off, or optional. When <code>ON</code>, all users must set up MFA before they can sign in. When <code>OPTIONAL</code>, your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose <code>OPTIONAL</code>.</p> <p>When <code>MfaConfiguration</code> is <code>OPTIONAL</code>, managed login doesn't automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.</p>"""
    web_authn_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.web_authn_configuration_type.WebAuthnConfigurationType"
    ]
    """<p>Shows user pool configuration for sign-in with passkey authenticators such as biometric devices and security keys. Includes relying-party configuration, user-verification requirements, and whether passkeys can satisfy MFA requirements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserPoolMfaConfigResponse) -> dict:
    out: dict = {}
    if "sms_mfa_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.sms_mfa_config_type

        out["SmsMfaConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.sms_mfa_config_type.serialize_aws_json_1_1(
                value["sms_mfa_configuration"]
            )
        )
    if "software_token_mfa_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.software_token_mfa_config_type

        out["SoftwareTokenMfaConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.software_token_mfa_config_type.serialize_aws_json_1_1(
                value["software_token_mfa_configuration"]
            )
        )
    if "email_mfa_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.email_mfa_config_type

        out["EmailMfaConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.email_mfa_config_type.serialize_aws_json_1_1(
                value["email_mfa_configuration"]
            )
        )
    if "mfa_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_mfa_type

        out["MfaConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_mfa_type.serialize_aws_json_1_1(
                value["mfa_configuration"]
            )
        )
    if "web_authn_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.web_authn_configuration_type

        out["WebAuthnConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.web_authn_configuration_type.serialize_aws_json_1_1(
                value["web_authn_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserPoolMfaConfigResponse:
    out: GetUserPoolMfaConfigResponse = {}  # type: ignore[typeddict-item]
    if "SmsMfaConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.sms_mfa_config_type

        out["sms_mfa_configuration"] = (
            aws_sdk_cognito_identity_provider.types.sms_mfa_config_type.deserialize_aws_json_1_1(
                data["SmsMfaConfiguration"]
            )
        )
    if "SoftwareTokenMfaConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.software_token_mfa_config_type

        out["software_token_mfa_configuration"] = (
            aws_sdk_cognito_identity_provider.types.software_token_mfa_config_type.deserialize_aws_json_1_1(
                data["SoftwareTokenMfaConfiguration"]
            )
        )
    if "EmailMfaConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.email_mfa_config_type

        out["email_mfa_configuration"] = (
            aws_sdk_cognito_identity_provider.types.email_mfa_config_type.deserialize_aws_json_1_1(
                data["EmailMfaConfiguration"]
            )
        )
    if "MfaConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_mfa_type

        out["mfa_configuration"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_mfa_type.deserialize_aws_json_1_1(
                data["MfaConfiguration"]
            )
        )
    if "WebAuthnConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.web_authn_configuration_type

        out["web_authn_configuration"] = (
            aws_sdk_cognito_identity_provider.types.web_authn_configuration_type.deserialize_aws_json_1_1(
                data["WebAuthnConfiguration"]
            )
        )
    return out
