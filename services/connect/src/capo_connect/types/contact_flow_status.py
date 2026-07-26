"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowStatus``."""

from typing import Literal, TypeAlias, cast

ContactFlowStatus: TypeAlias = Literal[
    "PUBLISHED",
    "SAVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowStatus) -> str:
    return value


def deserialize_json(data: str) -> ContactFlowStatus:
    return cast(ContactFlowStatus, data)
