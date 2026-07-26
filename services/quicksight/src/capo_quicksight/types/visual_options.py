"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string


class VisualOptions(TypedDict, closed=True):
    type: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The type for a <code>VisualOptions</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualOptions) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> VisualOptions:
    out: VisualOptions = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    return out
