"""Generated from Smithy shape ``com.amazonaws.guardduty#RemotePortDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string


class RemotePortDetails(TypedDict, closed=True):
    port: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The port number of the remote connection.</p>"""
    port_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The port name of the remote connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemotePortDetails) -> dict:
    out: dict = {}
    if "port" in value:
        out["port"] = value["port"]
    if "port_name" in value:
        out["portName"] = value["port_name"]
    return out


def deserialize_json(data: dict) -> RemotePortDetails:
    out: RemotePortDetails = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    if "portName" in data:
        out["port_name"] = data["portName"]
    return out
