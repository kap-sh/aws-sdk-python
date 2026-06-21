"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#FulfillmentState``."""

from typing import Literal, TypeAlias, cast

FulfillmentState: TypeAlias = Literal[
    "Fulfilled",
    "Failed",
    "ReadyForFulfillment",
]


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentState) -> str:
    return value


def deserialize_json(data: str) -> FulfillmentState:
    return cast(FulfillmentState, data)
