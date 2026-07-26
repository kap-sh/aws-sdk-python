"""Generated from Smithy shape ``com.amazonaws.xray#UnprocessedStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.unprocessed_statistics

UnprocessedStatisticsList: TypeAlias = list[
    "capo_xray.types.unprocessed_statistics.UnprocessedStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStatisticsList) -> list:
    import capo_xray.types.unprocessed_statistics

    out: list = []
    for item in value:
        out.append(capo_xray.types.unprocessed_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnprocessedStatisticsList:
    import capo_xray.types.unprocessed_statistics

    out: UnprocessedStatisticsList = []
    for item in data:
        out.append(capo_xray.types.unprocessed_statistics.deserialize_json(item))
    return out
