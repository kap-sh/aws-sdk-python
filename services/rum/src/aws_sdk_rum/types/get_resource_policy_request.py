"""Generated from Smithy shape ``com.amazonaws.rum#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name


class GetResourcePolicyRequest(TypedDict):
    name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the app monitor that is associated with the resource-based policy that you want to view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
