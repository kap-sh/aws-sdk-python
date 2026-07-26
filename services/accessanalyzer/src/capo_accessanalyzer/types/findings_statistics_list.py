"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingsStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.findings_statistics

FindingsStatisticsList: TypeAlias = list[
    "capo_accessanalyzer.types.findings_statistics.FindingsStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsStatisticsList) -> list:
    import capo_accessanalyzer.types.findings_statistics

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.findings_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingsStatisticsList:
    import capo_accessanalyzer.types.findings_statistics

    out: FindingsStatisticsList = []
    for item in data:
        out.append(capo_accessanalyzer.types.findings_statistics.deserialize_json(item))
    return out
