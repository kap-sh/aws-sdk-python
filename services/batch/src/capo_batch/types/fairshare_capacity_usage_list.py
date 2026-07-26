"""Generated from Smithy shape ``com.amazonaws.batch#FairshareCapacityUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.fairshare_capacity_usage

FairshareCapacityUsageList: TypeAlias = list[
    "capo_batch.types.fairshare_capacity_usage.FairshareCapacityUsage"
]


# --- restJson1 ser/de ---
def serialize_json(value: FairshareCapacityUsageList) -> list:
    import capo_batch.types.fairshare_capacity_usage

    out: list = []
    for item in value:
        out.append(capo_batch.types.fairshare_capacity_usage.serialize_json(item))
    return out


def deserialize_json(data: list) -> FairshareCapacityUsageList:
    import capo_batch.types.fairshare_capacity_usage

    out: FairshareCapacityUsageList = []
    for item in data:
        out.append(capo_batch.types.fairshare_capacity_usage.deserialize_json(item))
    return out
