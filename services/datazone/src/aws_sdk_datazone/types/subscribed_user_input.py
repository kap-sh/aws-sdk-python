"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedUserInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.user_profile_id


class SubscribedUserInput(TypedDict):
    identifier: NotRequired["aws_sdk_datazone.types.user_profile_id.UserProfileId"]
    """<p>The ID of the subscribed user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedUserInput) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> SubscribedUserInput:
    out: SubscribedUserInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    return out
