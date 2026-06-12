"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AccountTakeoverActionsType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.account_takeover_action_type


class AccountTakeoverActionsType(TypedDict):
    low_action: NotRequired[
        "aws_sdk_cognito_identity_provider.types.account_takeover_action_type.AccountTakeoverActionType"
    ]
    """<p>The action that you assign to a low-risk assessment by threat protection.</p>"""
    medium_action: NotRequired[
        "aws_sdk_cognito_identity_provider.types.account_takeover_action_type.AccountTakeoverActionType"
    ]
    """<p>The action that you assign to a medium-risk assessment by threat protection.</p>"""
    high_action: NotRequired[
        "aws_sdk_cognito_identity_provider.types.account_takeover_action_type.AccountTakeoverActionType"
    ]
    """<p>The action that you assign to a high-risk assessment by threat protection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountTakeoverActionsType) -> dict:
    out: dict = {}
    if "low_action" in value:
        import aws_sdk_cognito_identity_provider.types.account_takeover_action_type

        out["LowAction"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_action_type.serialize_aws_json_1_1(
                value["low_action"]
            )
        )
    if "medium_action" in value:
        import aws_sdk_cognito_identity_provider.types.account_takeover_action_type

        out["MediumAction"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_action_type.serialize_aws_json_1_1(
                value["medium_action"]
            )
        )
    if "high_action" in value:
        import aws_sdk_cognito_identity_provider.types.account_takeover_action_type

        out["HighAction"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_action_type.serialize_aws_json_1_1(
                value["high_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountTakeoverActionsType:
    out: AccountTakeoverActionsType = {}  # type: ignore[typeddict-item]
    if "LowAction" in data:
        import aws_sdk_cognito_identity_provider.types.account_takeover_action_type

        out["low_action"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_action_type.deserialize_aws_json_1_1(
                data["LowAction"]
            )
        )
    if "MediumAction" in data:
        import aws_sdk_cognito_identity_provider.types.account_takeover_action_type

        out["medium_action"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_action_type.deserialize_aws_json_1_1(
                data["MediumAction"]
            )
        )
    if "HighAction" in data:
        import aws_sdk_cognito_identity_provider.types.account_takeover_action_type

        out["high_action"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_action_type.deserialize_aws_json_1_1(
                data["HighAction"]
            )
        )
    return out
