"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateAccountPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.boolean_account_preference


class UpdateAccountPreferencesRequest(TypedDict, closed=True):
    user_authorization_required: NotRequired[
        "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
    ]
    """<p>Enables use of a user role requirement in your chat configuration.</p>"""
    training_data_collection_enabled: NotRequired[
        "capo_chatbot.types.boolean_account_preference.BooleanAccountPreference"
    ]
    """<p>Turns on training data collection.</p> <p>This helps improve the AWS Chatbot experience by allowing AWS Chatbot to store and use your customer information, such as AWS Chatbot configurations, notifications, user inputs, AWS Chatbot generated responses, and interaction data. This data helps us to continuously improve and develop Artificial Intelligence (AI) technologies. Your data is not shared with any third parties and is protected using sophisticated controls to prevent unauthorized access and misuse. AWS Chatbot does not store or use interactions in chat channels with Amazon Q for training AI technologies for AWS Chatbot. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountPreferencesRequest) -> dict:
    out: dict = {}
    if "user_authorization_required" in value:
        out["UserAuthorizationRequired"] = value["user_authorization_required"]
    if "training_data_collection_enabled" in value:
        out["TrainingDataCollectionEnabled"] = value["training_data_collection_enabled"]
    return out


def deserialize_json(data: dict) -> UpdateAccountPreferencesRequest:
    out: UpdateAccountPreferencesRequest = {}  # type: ignore[typeddict-item]
    if "UserAuthorizationRequired" in data:
        out["user_authorization_required"] = data["UserAuthorizationRequired"]
    if "TrainingDataCollectionEnabled" in data:
        out["training_data_collection_enabled"] = data["TrainingDataCollectionEnabled"]
    return out
