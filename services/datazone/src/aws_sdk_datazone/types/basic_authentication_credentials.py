"""Generated from Smithy shape ``com.amazonaws.datazone#BasicAuthenticationCredentials``."""

from typing import TypedDict
from typing_extensions import NotRequired


class BasicAuthenticationCredentials(TypedDict):
    user_name: NotRequired["str"]
    """<p>The user name for the connecion.</p>"""
    password: NotRequired["str"]
    """<p>The password for a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicAuthenticationCredentials) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "password" in value:
        out["password"] = value["password"]
    return out


def deserialize_json(data: dict) -> BasicAuthenticationCredentials:
    out: BasicAuthenticationCredentials = {}  # type: ignore[typeddict-item]
    if "userName" in data:
        out["user_name"] = data["userName"]
    if "password" in data:
        out["password"] = data["password"]
    return out
