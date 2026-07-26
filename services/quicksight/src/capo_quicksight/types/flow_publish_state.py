"""Generated from Smithy shape ``com.amazonaws.quicksight#FlowPublishState``."""

from typing import Literal, TypeAlias, cast

FlowPublishState: TypeAlias = Literal[
    "PUBLISHED",
    "DRAFT",
    "PENDING_APPROVAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowPublishState) -> str:
    return value


def deserialize_json(data: str) -> FlowPublishState:
    return cast(FlowPublishState, data)
