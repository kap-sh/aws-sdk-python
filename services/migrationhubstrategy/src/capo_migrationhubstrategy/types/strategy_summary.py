"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StrategySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.integer
    import capo_migrationhubstrategy.types.strategy


class StrategySummary(TypedDict, closed=True):
    strategy: NotRequired["capo_migrationhubstrategy.types.strategy.Strategy"]
    """<p> The name of recommended strategy. </p>"""
    count: NotRequired["capo_migrationhubstrategy.types.integer.Integer"]
    """<p> The count of recommendations per strategy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StrategySummary) -> dict:
    out: dict = {}
    if "strategy" in value:
        out["strategy"] = value["strategy"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> StrategySummary:
    out: StrategySummary = {}  # type: ignore[typeddict-item]
    if "strategy" in data:
        out["strategy"] = data["strategy"]
    if "count" in data:
        out["count"] = data["count"]
    return out
