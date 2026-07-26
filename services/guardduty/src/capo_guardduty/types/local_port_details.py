"""Generated from Smithy shape ``com.amazonaws.guardduty#LocalPortDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.string


class LocalPortDetails(TypedDict, closed=True):
    port: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The port number of the local connection.</p>"""
    port_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The port name of the local connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalPortDetails) -> dict:
    out: dict = {}
    if "port" in value:
        out["port"] = value["port"]
    if "port_name" in value:
        out["portName"] = value["port_name"]
    return out


def deserialize_json(data: dict) -> LocalPortDetails:
    out: LocalPortDetails = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    if "portName" in data:
        out["port_name"] = data["portName"]
    return out
