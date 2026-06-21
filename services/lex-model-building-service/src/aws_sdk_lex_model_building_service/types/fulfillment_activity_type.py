"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#FulfillmentActivityType``."""

from typing import Literal, TypeAlias, cast

FulfillmentActivityType: TypeAlias = Literal[
    "ReturnIntent",
    "CodeHook",
]


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentActivityType) -> str:
    return value


def deserialize_json(data: str) -> FulfillmentActivityType:
    return cast(FulfillmentActivityType, data)
