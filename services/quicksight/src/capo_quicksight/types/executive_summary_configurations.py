"""Generated from Smithy shape ``com.amazonaws.quicksight#ExecutiveSummaryConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean


class ExecutiveSummaryConfigurations(TypedDict, closed=True):
    enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>The executive summary settings of an embedded Quick Sight console or dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutiveSummaryConfigurations) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> ExecutiveSummaryConfigurations:
    out: ExecutiveSummaryConfigurations = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
