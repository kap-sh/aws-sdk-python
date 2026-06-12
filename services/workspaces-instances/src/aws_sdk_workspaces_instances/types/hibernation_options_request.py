"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HibernationOptionsRequest``."""

from typing import TypedDict
from typing_extensions import NotRequired

class HibernationOptionsRequest(TypedDict):
    configured: NotRequired["bool"]
    """<p>Enables or disables instance hibernation capability.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HibernationOptionsRequest) -> dict:
    out: dict = {}
    if "configured" in value:
        out["Configured"] = value["configured"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HibernationOptionsRequest:
    out: HibernationOptionsRequest = {}  # type: ignore[typeddict-item]
    if "Configured" in data:
        out["configured"] = data["Configured"]
    return out