"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.server_side_string


class CoreNetworkPolicyError(TypedDict, closed=True):
    error_code: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The error code associated with a core network policy error.</p>"""
    message: "capo_networkmanager.types.server_side_string.ServerSideString"
    """<p>The message associated with a core network policy error code.</p>"""
    path: NotRequired["capo_networkmanager.types.server_side_string.ServerSideString"]
    """<p>The JSON path where the error was discovered in the policy document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyError) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    out["Message"] = value["message"]
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_json(data: dict) -> CoreNetworkPolicyError:
    out: CoreNetworkPolicyError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("CoreNetworkPolicyError.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("CoreNetworkPolicyError.message required")
    if "Path" in data:
        out["path"] = data["Path"]
    return out
