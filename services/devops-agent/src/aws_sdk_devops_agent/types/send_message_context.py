"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageContext``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SendMessageContext(TypedDict):
    current_page: NotRequired["str"]
    """<p>The current page or view the user is on</p>"""
    last_message: NotRequired["str"]
    """<p>The ID of the last message in the conversation</p>"""
    user_action_response: NotRequired["str"]
    """<p>Response to a UI prompt (not a text conversation message)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageContext) -> dict:
    out: dict = {}
    if "current_page" in value:
        out["currentPage"] = value["current_page"]
    if "last_message" in value:
        out["lastMessage"] = value["last_message"]
    if "user_action_response" in value:
        out["userActionResponse"] = value["user_action_response"]
    return out


def deserialize_json(data: dict) -> SendMessageContext:
    out: SendMessageContext = {}  # type: ignore[typeddict-item]
    if "currentPage" in data:
        out["current_page"] = data["currentPage"]
    if "lastMessage" in data:
        out["last_message"] = data["lastMessage"]
    if "userActionResponse" in data:
        out["user_action_response"] = data["userActionResponse"]
    return out
