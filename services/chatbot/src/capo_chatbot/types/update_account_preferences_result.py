"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateAccountPreferencesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.account_preferences


class UpdateAccountPreferencesResult(TypedDict, closed=True):
    account_preferences: NotRequired[
        "capo_chatbot.types.account_preferences.AccountPreferences"
    ]
    """<p>Preferences related to AWS Chatbot usage in the calling AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountPreferencesResult) -> dict:
    out: dict = {}
    if "account_preferences" in value:
        import capo_chatbot.types.account_preferences

        out["AccountPreferences"] = (
            capo_chatbot.types.account_preferences.serialize_json(
                value["account_preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountPreferencesResult:
    out: UpdateAccountPreferencesResult = {}  # type: ignore[typeddict-item]
    if "AccountPreferences" in data:
        import capo_chatbot.types.account_preferences

        out["account_preferences"] = (
            capo_chatbot.types.account_preferences.deserialize_json(
                data["AccountPreferences"]
            )
        )
    return out
