"""Generated from Smithy shape ``com.amazonaws.pipes#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pipes.types.event_pattern


class Filter(TypedDict, closed=True):
    pattern: NotRequired["aws_sdk_pipes.types.event_pattern.EventPattern"]
    """<p>The event pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Pattern" in data:
        out["pattern"] = data["Pattern"]
    return out
