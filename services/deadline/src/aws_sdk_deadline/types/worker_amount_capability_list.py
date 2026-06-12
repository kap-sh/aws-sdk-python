"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerAmountCapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.worker_amount_capability

WorkerAmountCapabilityList: TypeAlias = list[
    "aws_sdk_deadline.types.worker_amount_capability.WorkerAmountCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkerAmountCapabilityList) -> list:
    import aws_sdk_deadline.types.worker_amount_capability

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.worker_amount_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkerAmountCapabilityList:
    import aws_sdk_deadline.types.worker_amount_capability

    out: WorkerAmountCapabilityList = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.worker_amount_capability.deserialize_json(item)
        )
    return out
