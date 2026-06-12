"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SmsMfaConfigType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.sms_configuration_type
    import aws_sdk_cognito_identity_provider.types.sms_verification_message_type


class SmsMfaConfigType(TypedDict):
    sms_authentication_message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.sms_verification_message_type.SmsVerificationMessageType"
    ]
    """<p>The SMS authentication message that will be sent to users with the code they must sign in with. The message must contain the <code>{####}</code> placeholder. Your user pool replaces the placeholder with the MFA code. If this parameter isn't provided, your user pool sends a default message.</p>"""
    sms_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.sms_configuration_type.SmsConfigurationType"
    ]
    """<p>User pool configuration for delivery of SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the Amazon Web Services Region that you want, the Amazon Cognito user pool uses an Identity and Access Management (IAM) role in your Amazon Web Services account.</p> <p>You can set <code>SmsConfiguration</code> in <code>CreateUserPool</code> and <code> UpdateUserPool</code>, or in <code>SetUserPoolMfaConfig</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SmsMfaConfigType) -> dict:
    out: dict = {}
    if "sms_authentication_message" in value:
        out["SmsAuthenticationMessage"] = value["sms_authentication_message"]
    if "sms_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.sms_configuration_type

        out["SmsConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.sms_configuration_type.serialize_aws_json_1_1(
                value["sms_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SmsMfaConfigType:
    out: SmsMfaConfigType = {}  # type: ignore[typeddict-item]
    if "SmsAuthenticationMessage" in data:
        out["sms_authentication_message"] = data["SmsAuthenticationMessage"]
    if "SmsConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.sms_configuration_type

        out["sms_configuration"] = (
            aws_sdk_cognito_identity_provider.types.sms_configuration_type.deserialize_aws_json_1_1(
                data["SmsConfiguration"]
            )
        )
    return out
