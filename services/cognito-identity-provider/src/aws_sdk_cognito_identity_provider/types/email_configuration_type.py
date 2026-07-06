"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EmailConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.arn_type
    import aws_sdk_cognito_identity_provider.types.email_address_type
    import aws_sdk_cognito_identity_provider.types.email_sending_account_type
    import aws_sdk_cognito_identity_provider.types.ses_configuration_set
    import aws_sdk_cognito_identity_provider.types.string_type

EmailConfigurationType = TypedDict(
    "EmailConfigurationType",
    {
        "source_arn": NotRequired[
            "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
        ],
        "reply_to_email_address": NotRequired[
            "aws_sdk_cognito_identity_provider.types.email_address_type.EmailAddressType"
        ],
        "email_sending_account": NotRequired[
            "aws_sdk_cognito_identity_provider.types.email_sending_account_type.EmailSendingAccountType"
        ],
        "from": NotRequired[
            "aws_sdk_cognito_identity_provider.types.string_type.StringType"
        ],
        "configuration_set": NotRequired[
            "aws_sdk_cognito_identity_provider.types.ses_configuration_set.SESConfigurationSet"
        ],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmailConfigurationType) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "reply_to_email_address" in value:
        out["ReplyToEmailAddress"] = value["reply_to_email_address"]
    if "email_sending_account" in value:
        import aws_sdk_cognito_identity_provider.types.email_sending_account_type

        out["EmailSendingAccount"] = (
            aws_sdk_cognito_identity_provider.types.email_sending_account_type.serialize_aws_json_1_1(
                value["email_sending_account"]
            )
        )
    if "from" in value:
        out["From"] = value["from"]
    if "configuration_set" in value:
        out["ConfigurationSet"] = value["configuration_set"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EmailConfigurationType:
    out: EmailConfigurationType = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "ReplyToEmailAddress" in data:
        out["reply_to_email_address"] = data["ReplyToEmailAddress"]
    if "EmailSendingAccount" in data:
        import aws_sdk_cognito_identity_provider.types.email_sending_account_type

        out["email_sending_account"] = (
            aws_sdk_cognito_identity_provider.types.email_sending_account_type.deserialize_aws_json_1_1(
                data["EmailSendingAccount"]
            )
        )
    if "From" in data:
        out["from"] = data["From"]
    if "ConfigurationSet" in data:
        out["configuration_set"] = data["ConfigurationSet"]
    return out
