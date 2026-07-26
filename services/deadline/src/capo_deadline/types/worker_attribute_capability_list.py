"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerAttributeCapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.worker_attribute_capability

WorkerAttributeCapabilityList: TypeAlias = list[
    "capo_deadline.types.worker_attribute_capability.WorkerAttributeCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkerAttributeCapabilityList) -> list:
    import capo_deadline.types.worker_attribute_capability

    out: list = []
    for item in value:
        out.append(capo_deadline.types.worker_attribute_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkerAttributeCapabilityList:
    import capo_deadline.types.worker_attribute_capability

    out: WorkerAttributeCapabilityList = []
    for item in data:
        out.append(
            capo_deadline.types.worker_attribute_capability.deserialize_json(item)
        )
    return out
