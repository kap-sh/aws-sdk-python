"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListStrategySummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.strategy_summary

ListStrategySummary: TypeAlias = list[
    "capo_migrationhubstrategy.types.strategy_summary.StrategySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListStrategySummary) -> list:
    import capo_migrationhubstrategy.types.strategy_summary

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.strategy_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListStrategySummary:
    import capo_migrationhubstrategy.types.strategy_summary

    out: ListStrategySummary = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.strategy_summary.deserialize_json(item)
        )
    return out
