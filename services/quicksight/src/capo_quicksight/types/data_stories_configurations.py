"""Generated from Smithy shape ``com.amazonaws.quicksight#DataStoriesConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean


class DataStoriesConfigurations(TypedDict, closed=True):
    enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>The data story settings of an embedded Quick Sight console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataStoriesConfigurations) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> DataStoriesConfigurations:
    out: DataStoriesConfigurations = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
