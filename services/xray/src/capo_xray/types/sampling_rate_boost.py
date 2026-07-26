"""Generated from Smithy shape ``com.amazonaws.xray#SamplingRateBoost``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.cooldown_window_minutes
    import capo_xray.types.max_rate


class SamplingRateBoost(TypedDict, closed=True):
    max_rate: "capo_xray.types.max_rate.MaxRate"
    """<p>Defines max temporary sampling rate to apply when a boost is triggered. Calculated boost rate by X-Ray will be less than or equal to this max rate.</p>"""
    cooldown_window_minutes: (
        "capo_xray.types.cooldown_window_minutes.CooldownWindowMinutes"
    )
    """<p>Sets the time window (in minutes) in which only one sampling rate boost can be triggered. After a boost occurs, no further boosts are allowed until the next window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingRateBoost) -> dict:
    out: dict = {}
    out["MaxRate"] = value.get("max_rate", 0)
    out["CooldownWindowMinutes"] = value.get("cooldown_window_minutes", 0)
    return out


def deserialize_json(data: dict) -> SamplingRateBoost:
    out: SamplingRateBoost = {}  # type: ignore[typeddict-item]
    if "MaxRate" in data:
        out["max_rate"] = data["MaxRate"]
    else:
        out["max_rate"] = 0
    if "CooldownWindowMinutes" in data:
        out["cooldown_window_minutes"] = data["CooldownWindowMinutes"]
    else:
        out["cooldown_window_minutes"] = 0
    return out
