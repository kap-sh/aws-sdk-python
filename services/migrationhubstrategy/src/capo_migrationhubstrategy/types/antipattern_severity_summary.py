"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AntipatternSeveritySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.integer
    import capo_migrationhubstrategy.types.severity


class AntipatternSeveritySummary(TypedDict, closed=True):
    severity: NotRequired["capo_migrationhubstrategy.types.severity.Severity"]
    """<p> Contains the severity of anti-patterns. </p>"""
    count: NotRequired["capo_migrationhubstrategy.types.integer.Integer"]
    """<p> Contains the count of anti-patterns. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AntipatternSeveritySummary) -> dict:
    out: dict = {}
    if "severity" in value:
        out["severity"] = value["severity"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> AntipatternSeveritySummary:
    out: AntipatternSeveritySummary = {}  # type: ignore[typeddict-item]
    if "severity" in data:
        out["severity"] = data["severity"]
    if "count" in data:
        out["count"] = data["count"]
    return out
