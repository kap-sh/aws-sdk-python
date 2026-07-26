"""Generated from Smithy shape ``com.amazonaws.securityhub#PortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class PortRange(TypedDict, closed=True):
    begin: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The first port in the port range.</p>"""
    end: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The last port in the port range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortRange) -> dict:
    out: dict = {}
    if "begin" in value:
        out["Begin"] = value["begin"]
    if "end" in value:
        out["End"] = value["end"]
    return out


def deserialize_json(data: dict) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    if "Begin" in data:
        out["begin"] = data["Begin"]
    if "End" in data:
        out["end"] = data["End"]
    return out
