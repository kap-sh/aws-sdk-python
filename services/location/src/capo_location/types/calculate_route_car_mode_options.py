"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteCarModeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.sensitive_boolean


class CalculateRouteCarModeOptions(TypedDict, closed=True):
    avoid_ferries: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoids ferries when calculating routes.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    avoid_tolls: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoids tolls when calculating routes.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteCarModeOptions) -> dict:
    out: dict = {}
    if "avoid_ferries" in value:
        out["AvoidFerries"] = value["avoid_ferries"]
    if "avoid_tolls" in value:
        out["AvoidTolls"] = value["avoid_tolls"]
    return out


def deserialize_json(data: dict) -> CalculateRouteCarModeOptions:
    out: CalculateRouteCarModeOptions = {}  # type: ignore[typeddict-item]
    if "AvoidFerries" in data:
        out["avoid_ferries"] = data["AvoidFerries"]
    if "AvoidTolls" in data:
        out["avoid_tolls"] = data["AvoidTolls"]
    return out
