"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AccountTakeoverActionsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.account_takeover_action_type


class AccountTakeoverActionsType(TypedDict, closed=True):
    low_action: NotRequired[
        "capo_cognito_identity_provider.types.account_takeover_action_type.AccountTakeoverActionType"
    ]
    """<p>The action that you assign to a low-risk assessment by threat protection.</p>"""
    medium_action: NotRequired[
        "capo_cognito_identity_provider.types.account_takeover_action_type.AccountTakeoverActionType"
    ]
    """<p>The action that you assign to a medium-risk assessment by threat protection.</p>"""
    high_action: NotRequired[
        "capo_cognito_identity_provider.types.account_takeover_action_type.AccountTakeoverActionType"
    ]
    """<p>The action that you assign to a high-risk assessment by threat protection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountTakeoverActionsType) -> dict:
    out: dict = {}
    if "low_action" in value:
        import capo_cognito_identity_provider.types.account_takeover_action_type

        out["LowAction"] = (
            capo_cognito_identity_provider.types.account_takeover_action_type.serialize_aws_json_1_1(
                value["low_action"]
            )
        )
    if "medium_action" in value:
        import capo_cognito_identity_provider.types.account_takeover_action_type

        out["MediumAction"] = (
            capo_cognito_identity_provider.types.account_takeover_action_type.serialize_aws_json_1_1(
                value["medium_action"]
            )
        )
    if "high_action" in value:
        import capo_cognito_identity_provider.types.account_takeover_action_type

        out["HighAction"] = (
            capo_cognito_identity_provider.types.account_takeover_action_type.serialize_aws_json_1_1(
                value["high_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountTakeoverActionsType:
    out: AccountTakeoverActionsType = {}  # type: ignore[typeddict-item]
    if "LowAction" in data:
        import capo_cognito_identity_provider.types.account_takeover_action_type

        out["low_action"] = (
            capo_cognito_identity_provider.types.account_takeover_action_type.deserialize_aws_json_1_1(
                data["LowAction"]
            )
        )
    if "MediumAction" in data:
        import capo_cognito_identity_provider.types.account_takeover_action_type

        out["medium_action"] = (
            capo_cognito_identity_provider.types.account_takeover_action_type.deserialize_aws_json_1_1(
                data["MediumAction"]
            )
        )
    if "HighAction" in data:
        import capo_cognito_identity_provider.types.account_takeover_action_type

        out["high_action"] = (
            capo_cognito_identity_provider.types.account_takeover_action_type.deserialize_aws_json_1_1(
                data["HighAction"]
            )
        )
    return out
