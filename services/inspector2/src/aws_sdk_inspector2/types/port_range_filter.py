"""Generated from Smithy shape ``com.amazonaws.inspector2#PortRangeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.port


class PortRangeFilter(TypedDict):
    begin_inclusive: NotRequired["aws_sdk_inspector2.types.port.Port"]
    """<p>The port number the port range begins at.</p>"""
    end_inclusive: NotRequired["aws_sdk_inspector2.types.port.Port"]
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
