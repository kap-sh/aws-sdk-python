"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#NotifyConfigurationType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.arn_type
    import aws_sdk_cognito_identity_provider.types.notify_email_type
    import aws_sdk_cognito_identity_provider.types.string_type

NotifyConfigurationType = TypedDict(
    "NotifyConfigurationType",
    {
        "from": NotRequired[
            "aws_sdk_cognito_identity_provider.types.string_type.StringType"
        ],
        "reply_to": NotRequired[
            "aws_sdk_cognito_identity_provider.types.string_type.StringType"
        ],
        "source_arn": "aws_sdk_cognito_identity_provider.types.arn_type.ArnType",
        "block_email": NotRequired[
            "aws_sdk_cognito_identity_provider.types.notify_email_type.NotifyEmailType"
        ],
        "no_action_email": NotRequired[
            "aws_sdk_cognito_identity_provider.types.notify_email_type.NotifyEmailType"
        ],
        "mfa_email": NotRequired[
            "aws_sdk_cognito_identity_provider.types.notify_email_type.NotifyEmailType"
        ],
    },
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyConfigurationType) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = value["from"]
    if "reply_to" in value:
        out["ReplyTo"] = value["reply_to"]
    out["SourceArn"] = value["source_arn"]
    if "block_email" in value:
        import aws_sdk_cognito_identity_provider.types.notify_email_type

        out["BlockEmail"] = (
            aws_sdk_cognito_identity_provider.types.notify_email_type.serialize_aws_json_1_1(
                value["block_email"]
            )
        )
    if "no_action_email" in value:
        import aws_sdk_cognito_identity_provider.types.notify_email_type

        out["NoActionEmail"] = (
            aws_sdk_cognito_identity_provider.types.notify_email_type.serialize_aws_json_1_1(
                value["no_action_email"]
            )
        )
    if "mfa_email" in value:
        import aws_sdk_cognito_identity_provider.types.notify_email_type

        out["MfaEmail"] = (
            aws_sdk_cognito_identity_provider.types.notify_email_type.serialize_aws_json_1_1(
                value["mfa_email"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyConfigurationType:
    out: NotifyConfigurationType = {}  # type: ignore[typeddict-item]
    if "From" in data:
        out["from"] = data["From"]
    if "ReplyTo" in data:
        out["reply_to"] = data["ReplyTo"]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    else:
        raise DeserializationError("NotifyConfigurationType.source_arn required")
    if "BlockEmail" in data:
        import aws_sdk_cognito_identity_provider.types.notify_email_type

        out["block_email"] = (
            aws_sdk_cognito_identity_provider.types.notify_email_type.deserialize_aws_json_1_1(
                data["BlockEmail"]
            )
        )
    if "NoActionEmail" in data:
        import aws_sdk_cognito_identity_provider.types.notify_email_type

        out["no_action_email"] = (
            aws_sdk_cognito_identity_provider.types.notify_email_type.deserialize_aws_json_1_1(
                data["NoActionEmail"]
            )
        )
    if "MfaEmail" in data:
        import aws_sdk_cognito_identity_provider.types.notify_email_type

        out["mfa_email"] = (
            aws_sdk_cognito_identity_provider.types.notify_email_type.deserialize_aws_json_1_1(
                data["MfaEmail"]
            )
        )
    return out
