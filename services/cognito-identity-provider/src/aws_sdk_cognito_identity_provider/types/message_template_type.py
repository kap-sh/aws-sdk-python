"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#MessageTemplateType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.email_invite_message_type
    import aws_sdk_cognito_identity_provider.types.email_verification_subject_type
    import aws_sdk_cognito_identity_provider.types.sms_invite_message_type


class MessageTemplateType(TypedDict):
    sms_message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.sms_invite_message_type.SmsInviteMessageType"
    ]
    """<p>The message template for SMS messages.</p>"""
    email_message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.email_invite_message_type.EmailInviteMessageType"
    ]
    """<p>The message template for email messages. EmailMessage is allowed only if <a href=\"https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount\">EmailSendingAccount</a> is DEVELOPER. </p>"""
    email_subject: NotRequired[
        "aws_sdk_cognito_identity_provider.types.email_verification_subject_type.EmailVerificationSubjectType"
    ]
    """<p>The subject line for email messages. EmailSubject is allowed only if <a href=\"https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount\">EmailSendingAccount</a> is DEVELOPER. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MessageTemplateType) -> dict:
    out: dict = {}
    if "sms_message" in value:
        out["SMSMessage"] = value["sms_message"]
    if "email_message" in value:
        out["EmailMessage"] = value["email_message"]
    if "email_subject" in value:
        out["EmailSubject"] = value["email_subject"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MessageTemplateType:
    out: MessageTemplateType = {}  # type: ignore[typeddict-item]
    if "SMSMessage" in data:
        out["sms_message"] = data["SMSMessage"]
    if "EmailMessage" in data:
        out["email_message"] = data["EmailMessage"]
    if "EmailSubject" in data:
        out["email_subject"] = data["EmailSubject"]
    return out
