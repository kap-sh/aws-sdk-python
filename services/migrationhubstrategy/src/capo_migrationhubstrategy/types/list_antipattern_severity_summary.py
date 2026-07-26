"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListAntipatternSeveritySummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.antipattern_severity_summary

ListAntipatternSeveritySummary: TypeAlias = list[
    "capo_migrationhubstrategy.types.antipattern_severity_summary.AntipatternSeveritySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAntipatternSeveritySummary) -> list:
    import capo_migrationhubstrategy.types.antipattern_severity_summary

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.antipattern_severity_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListAntipatternSeveritySummary:
    import capo_migrationhubstrategy.types.antipattern_severity_summary

    out: ListAntipatternSeveritySummary = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.antipattern_severity_summary.deserialize_json(
                item
            )
        )
    return out
