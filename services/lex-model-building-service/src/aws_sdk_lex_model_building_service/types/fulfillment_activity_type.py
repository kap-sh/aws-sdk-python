"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#FulfillmentActivityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

FulfillmentActivityType: TypeAlias = Literal[
    "ReturnIntent",
    "CodeHook",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ReturnIntent",
        "CodeHook",
    )
)


def serialize_json(value: FulfillmentActivityType) -> str:
    return value


def deserialize_json(data: str) -> FulfillmentActivityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FulfillmentActivityType value: {data!r}")
    return cast(FulfillmentActivityType, data)
