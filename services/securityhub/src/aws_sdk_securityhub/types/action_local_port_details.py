"""Generated from Smithy shape ``com.amazonaws.securityhub#ActionLocalPortDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class ActionLocalPortDetails(TypedDict, closed=True):
    port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of the port.</p>"""
    port_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The port name of the local connection.</p> <p>Length Constraints: 128.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionLocalPortDetails) -> dict:
    out: dict = {}
    if "port" in value:
        out["Port"] = value["port"]
    if "port_name" in value:
        out["PortName"] = value["port_name"]
    return out


def deserialize_json(data: dict) -> ActionLocalPortDetails:
    out: ActionLocalPortDetails = {}  # type: ignore[typeddict-item]
    if "Port" in data:
        out["port"] = data["Port"]
    if "PortName" in data:
        out["port_name"] = data["PortName"]
    return out
