"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#IntentState``."""

from typing import Literal, TypeAlias, cast

IntentState: TypeAlias = Literal[
    "Failed",
    "Fulfilled",
    "InProgress",
    "ReadyForFulfillment",
    "Waiting",
    "FulfillmentInProgress",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentState) -> str:
    return value


def deserialize_json(data: str) -> IntentState:
    return cast(IntentState, data)
