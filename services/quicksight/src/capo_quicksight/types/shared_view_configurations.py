"""Generated from Smithy shape ``com.amazonaws.quicksight#SharedViewConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean


class SharedViewConfigurations(TypedDict, closed=True):
    enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>The shared view settings of an embedded dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharedViewConfigurations) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> SharedViewConfigurations:
    out: SharedViewConfigurations = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
