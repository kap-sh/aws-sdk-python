"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateAccountPreferencesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.account_preferences


class UpdateAccountPreferencesResult(TypedDict):
    account_preferences: NotRequired[
        "aws_sdk_chatbot.types.account_preferences.AccountPreferences"
    ]
    """<p>Preferences related to AWS Chatbot usage in the calling AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountPreferencesResult) -> dict:
    out: dict = {}
    if "account_preferences" in value:
        import aws_sdk_chatbot.types.account_preferences

        out["AccountPreferences"] = (
            aws_sdk_chatbot.types.account_preferences.serialize_json(
                value["account_preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountPreferencesResult:
    out: UpdateAccountPreferencesResult = {}  # type: ignore[typeddict-item]
    if "AccountPreferences" in data:
        import aws_sdk_chatbot.types.account_preferences

        out["account_preferences"] = (
            aws_sdk_chatbot.types.account_preferences.deserialize_json(
                data["AccountPreferences"]
            )
        )
    return out
