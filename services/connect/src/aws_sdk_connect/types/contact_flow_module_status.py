"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleStatus``."""

from typing import Literal, TypeAlias, cast

ContactFlowModuleStatus: TypeAlias = Literal[
    "PUBLISHED",
    "SAVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleStatus) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowModuleStatus:
    return cast(ContactFlowModuleStatus, data)
