"""Generated from Smithy shape ``com.amazonaws.batch#SchedulingPolicyDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.scheduling_policy_detail

SchedulingPolicyDetailList: TypeAlias = list[
    "capo_batch.types.scheduling_policy_detail.SchedulingPolicyDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingPolicyDetailList) -> list:
    import capo_batch.types.scheduling_policy_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.scheduling_policy_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchedulingPolicyDetailList:
    import capo_batch.types.scheduling_policy_detail

    out: SchedulingPolicyDetailList = []
    for item in data:
        out.append(capo_batch.types.scheduling_policy_detail.deserialize_json(item))
    return out
