"""Generated from Smithy shape ``com.amazonaws.connect#UserInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_resource_id


class UserInfo(TypedDict, closed=True):
    user_id: NotRequired["aws_sdk_connect.types.agent_resource_id.AgentResourceId"]
    """<p>The user identifier for the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserInfo) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> UserInfo:
    out: UserInfo = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    return out
