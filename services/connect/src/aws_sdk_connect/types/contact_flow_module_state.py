"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleState``."""

from typing import Literal, TypeAlias, cast

ContactFlowModuleState: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleState) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowModuleState:
    return cast(ContactFlowModuleState, data)
