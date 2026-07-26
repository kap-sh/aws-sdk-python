"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#Collectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.collector

Collectors: TypeAlias = list["capo_migrationhubstrategy.types.collector.Collector"]


# --- restJson1 ser/de ---
def serialize_json(value: Collectors) -> list:
    import capo_migrationhubstrategy.types.collector

    out: list = []
    for item in value:
        out.append(capo_migrationhubstrategy.types.collector.serialize_json(item))
    return out


def deserialize_json(data: list) -> Collectors:
    import capo_migrationhubstrategy.types.collector

    out: Collectors = []
    for item in data:
        out.append(capo_migrationhubstrategy.types.collector.deserialize_json(item))
    return out
