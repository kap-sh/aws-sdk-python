"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingWorkflowsSupported``."""

from typing import TypeAlias

IdMappingWorkflowsSupported: TypeAlias = list["object"]


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowsSupported) -> list:
    return list(value)


def deserialize_json(data: list) -> IdMappingWorkflowsSupported:
    return list(data)
