"""Generated from Smithy shape ``com.amazonaws.quicksight#ThresholdAlertsConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean


class ThresholdAlertsConfigurations(TypedDict, closed=True):
    enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>The threshold alerts configuration for an embedded Quick Sight dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThresholdAlertsConfigurations) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> ThresholdAlertsConfigurations:
    out: ThresholdAlertsConfigurations = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
