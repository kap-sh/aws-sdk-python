"""Generated from Smithy shape ``com.amazonaws.oam#ResourceTypesOutput``."""

from typing import TypeAlias

ResourceTypesOutput: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypesOutput) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceTypesOutput:
    return list(data)
