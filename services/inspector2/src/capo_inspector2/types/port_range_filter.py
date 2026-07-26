"""Generated from Smithy shape ``com.amazonaws.inspector2#PortRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.port


class PortRangeFilter(TypedDict, closed=True):
    begin_inclusive: NotRequired["capo_inspector2.types.port.Port"]
    """<p>The port number the port range begins at.</p>"""
    end_inclusive: NotRequired["capo_inspector2.types.port.Port"]
    """<p>The port number the port range ends at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortRangeFilter) -> dict:
    out: dict = {}
    if "begin_inclusive" in value:
        out["beginInclusive"] = value["begin_inclusive"]
    if "end_inclusive" in value:
        out["endInclusive"] = value["end_inclusive"]
    return out


def deserialize_json(data: dict) -> PortRangeFilter:
    out: PortRangeFilter = {}  # type: ignore[typeddict-item]
    if "beginInclusive" in data:
        out["begin_inclusive"] = data["beginInclusive"]
    if "endInclusive" in data:
        out["end_inclusive"] = data["endInclusive"]
    return out
