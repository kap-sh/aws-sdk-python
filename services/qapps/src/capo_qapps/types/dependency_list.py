"""Generated from Smithy shape ``com.amazonaws.qapps#DependencyList``."""

from typing import TypeAlias

DependencyList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyList) -> list:
    return list(value)


def deserialize_json(data: list) -> DependencyList:
    return list(data)
