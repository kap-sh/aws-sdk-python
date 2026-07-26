"""Generated from Smithy shape ``com.amazonaws.connect#UserQuickConnectConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id
    import capo_connect.types.user_id


class UserQuickConnectConfig(TypedDict, closed=True):
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserQuickConnectConfig) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> UserQuickConnectConfig:
    out: UserQuickConnectConfig = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("UserQuickConnectConfig.user_id required")
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("UserQuickConnectConfig.contact_flow_id required")
    return out
