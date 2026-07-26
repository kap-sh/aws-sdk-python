"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsTopContributorsTimestampsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import datetime

WorkloadInsightsTopContributorsTimestampsList: TypeAlias = list["datetime.datetime"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadInsightsTopContributorsTimestampsList) -> list:
    import capo_networkflowmonitor.types._prelude.timestamp

    out: list = []
    for item in value:
        out.append(
            capo_networkflowmonitor.types._prelude.timestamp.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkloadInsightsTopContributorsTimestampsList:
    import capo_networkflowmonitor.types._prelude.timestamp

    out: WorkloadInsightsTopContributorsTimestampsList = []
    for item in data:
        out.append(
            capo_networkflowmonitor.types._prelude.timestamp.deserialize_json(item)
        )
    return out
