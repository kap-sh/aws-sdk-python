"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowState``."""

from typing import Literal, TypeAlias, cast

ContactFlowState: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowState) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowState:
    return cast(ContactFlowState, data)
