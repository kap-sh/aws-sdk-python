"""Generated from Smithy shape ``com.amazonaws.chatbot#GetAccountPreferencesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.account_preferences


class GetAccountPreferencesResult(TypedDict):
    account_preferences: NotRequired[
        "aws_sdk_chatbot.types.account_preferences.AccountPreferences"
    ]
    """<p>The preferences related to AWS Chatbot usage in the calling AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountPreferencesResult) -> dict:
    out: dict = {}
    if "account_preferences" in value:
        import aws_sdk_chatbot.types.account_preferences

        out["AccountPreferences"] = (
            aws_sdk_chatbot.types.account_preferences.serialize_json(
                value["account_preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAccountPreferencesResult:
    out: GetAccountPreferencesResult = {}  # type: ignore[typeddict-item]
    if "AccountPreferences" in data:
        import aws_sdk_chatbot.types.account_preferences

        out["account_preferences"] = (
            aws_sdk_chatbot.types.account_preferences.deserialize_json(
                data["AccountPreferences"]
            )
        )
    return out
