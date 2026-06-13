"""Generated from Smithy shape ``com.amazonaws.devopsagent#DynatraceResourceList``."""

from typing import TypeAlias

DynatraceResourceList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceResourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> DynatraceResourceList:
    return list(data)
