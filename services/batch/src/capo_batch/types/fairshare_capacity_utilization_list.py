"""Generated from Smithy shape ``com.amazonaws.batch#FairshareCapacityUtilizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.fairshare_capacity_utilization

FairshareCapacityUtilizationList: TypeAlias = list[
    "capo_batch.types.fairshare_capacity_utilization.FairshareCapacityUtilization"
]


# --- restJson1 ser/de ---
def serialize_json(value: FairshareCapacityUtilizationList) -> list:
    import capo_batch.types.fairshare_capacity_utilization

    out: list = []
    for item in value:
        out.append(capo_batch.types.fairshare_capacity_utilization.serialize_json(item))
    return out


def deserialize_json(data: list) -> FairshareCapacityUtilizationList:
    import capo_batch.types.fairshare_capacity_utilization

    out: FairshareCapacityUtilizationList = []
    for item in data:
        out.append(
            capo_batch.types.fairshare_capacity_utilization.deserialize_json(item)
        )
    return out
