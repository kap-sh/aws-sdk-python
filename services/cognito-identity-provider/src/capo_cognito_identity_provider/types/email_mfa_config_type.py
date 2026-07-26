"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EmailMfaConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.email_mfa_message_type
    import capo_cognito_identity_provider.types.email_mfa_subject_type


class EmailMfaConfigType(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.email_mfa_message_type.EmailMfaMessageType"
    ]
    """<p>The template for the email messages that your user pool sends to users with codes for MFA and sign-in with email OTPs. The message must contain the <code>{####}</code> placeholder. In the message, Amazon Cognito replaces this placeholder with the code. If you don't provide this parameter, Amazon Cognito sends messages in the default format.</p>"""
    subject: NotRequired[
        "capo_cognito_identity_provider.types.email_mfa_subject_type.EmailMfaSubjectType"
    ]
    """<p>The subject of the email messages that your user pool sends to users with codes for MFA and email OTP sign-in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmailMfaConfigType) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EmailMfaConfigType:
    out: EmailMfaConfigType = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    return out
