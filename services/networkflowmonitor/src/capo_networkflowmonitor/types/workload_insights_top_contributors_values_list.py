"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsTopContributorsValuesList``."""

from typing import TypeAlias

WorkloadInsightsTopContributorsValuesList: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadInsightsTopContributorsValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadInsightsTopContributorsValuesList:
    return list(data)
