"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AccountTakeoverRiskConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.account_takeover_actions_type
    import aws_sdk_cognito_identity_provider.types.notify_configuration_type


class AccountTakeoverRiskConfigurationType(TypedDict, closed=True):
    notify_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.notify_configuration_type.NotifyConfigurationType"
    ]
    """<p>The settings for composing and sending an email message when threat protection assesses a risk level with adaptive authentication. When you choose to notify users in <code>AccountTakeoverRiskConfiguration</code>, Amazon Cognito sends an email message using the method and template that you set with this data type.</p>"""
    actions: "aws_sdk_cognito_identity_provider.types.account_takeover_actions_type.AccountTakeoverActionsType"
    """<p>A list of account-takeover actions for each level of risk that Amazon Cognito might assess with threat protection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountTakeoverRiskConfigurationType) -> dict:
    out: dict = {}
    if "notify_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.notify_configuration_type

        out["NotifyConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.notify_configuration_type.serialize_aws_json_1_1(
                value["notify_configuration"]
            )
        )
    import aws_sdk_cognito_identity_provider.types.account_takeover_actions_type

    out["Actions"] = (
        aws_sdk_cognito_identity_provider.types.account_takeover_actions_type.serialize_aws_json_1_1(
            value["actions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountTakeoverRiskConfigurationType:
    out: AccountTakeoverRiskConfigurationType = {}  # type: ignore[typeddict-item]
    if "NotifyConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.notify_configuration_type

        out["notify_configuration"] = (
            aws_sdk_cognito_identity_provider.types.notify_configuration_type.deserialize_aws_json_1_1(
                data["NotifyConfiguration"]
            )
        )
    if "Actions" in data:
        import aws_sdk_cognito_identity_provider.types.account_takeover_actions_type

        out["actions"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_actions_type.deserialize_aws_json_1_1(
                data["Actions"]
            )
        )
    else:
        raise DeserializationError(
            "AccountTakeoverRiskConfigurationType.actions required"
        )
    return out
