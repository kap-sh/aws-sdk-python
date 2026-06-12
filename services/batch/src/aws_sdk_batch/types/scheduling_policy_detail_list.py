"""Generated from Smithy shape ``com.amazonaws.batch#SchedulingPolicyDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.scheduling_policy_detail

SchedulingPolicyDetailList: TypeAlias = list[
    "aws_sdk_batch.types.scheduling_policy_detail.SchedulingPolicyDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingPolicyDetailList) -> list:
    import aws_sdk_batch.types.scheduling_policy_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.scheduling_policy_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchedulingPolicyDetailList:
    import aws_sdk_batch.types.scheduling_policy_detail

    out: SchedulingPolicyDetailList = []
    for item in data:
        out.append(aws_sdk_batch.types.scheduling_policy_detail.deserialize_json(item))
    return out
