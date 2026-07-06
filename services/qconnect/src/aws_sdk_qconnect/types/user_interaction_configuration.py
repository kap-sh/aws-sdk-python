"""Generated from Smithy shape ``com.amazonaws.qconnect#UserInteractionConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class UserInteractionConfiguration(TypedDict, closed=True):
    is_user_confirmation_required: NotRequired["bool"]
    """<p>Indicates whether user confirmation is required for the interaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserInteractionConfiguration) -> dict:
    out: dict = {}
    if "is_user_confirmation_required" in value:
        out["isUserConfirmationRequired"] = value["is_user_confirmation_required"]
    return out


def deserialize_json(data: dict) -> UserInteractionConfiguration:
    out: UserInteractionConfiguration = {}  # type: ignore[typeddict-item]
    if "isUserConfirmationRequired" in data:
        out["is_user_confirmation_required"] = data["isUserConfirmationRequired"]
    return out
