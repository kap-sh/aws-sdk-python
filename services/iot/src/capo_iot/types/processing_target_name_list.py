"""Generated from Smithy shape ``com.amazonaws.iot#ProcessingTargetNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.processing_target_name

ProcessingTargetNameList: TypeAlias = list[
    "capo_iot.types.processing_target_name.ProcessingTargetName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProcessingTargetNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ProcessingTargetNameList:
    return list(data)
