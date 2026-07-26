"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedAccessTypeStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.unused_access_type_statistics

UnusedAccessTypeStatisticsList: TypeAlias = list[
    "capo_accessanalyzer.types.unused_access_type_statistics.UnusedAccessTypeStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnusedAccessTypeStatisticsList) -> list:
    import capo_accessanalyzer.types.unused_access_type_statistics

    out: list = []
    for item in value:
        out.append(
            capo_accessanalyzer.types.unused_access_type_statistics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UnusedAccessTypeStatisticsList:
    import capo_accessanalyzer.types.unused_access_type_statistics

    out: UnusedAccessTypeStatisticsList = []
    for item in data:
        out.append(
            capo_accessanalyzer.types.unused_access_type_statistics.deserialize_json(
                item
            )
        )
    return out
