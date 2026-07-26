"""Generated from Smithy shape ``com.amazonaws.tnb#NsLcmOperationState``."""

from typing import Literal, TypeAlias, cast

NsLcmOperationState: TypeAlias = Literal[
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "CANCELLING",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NsLcmOperationState) -> str:
    return value


def deserialize_json(data: str) -> NsLcmOperationState:
    return cast(NsLcmOperationState, data)
