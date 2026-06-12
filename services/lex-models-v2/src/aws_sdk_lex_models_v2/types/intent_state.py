"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

IntentState: TypeAlias = Literal[
    "Failed",
    "Fulfilled",
    "InProgress",
    "ReadyForFulfillment",
    "Waiting",
    "FulfillmentInProgress",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Failed",
        "Fulfilled",
        "InProgress",
        "ReadyForFulfillment",
        "Waiting",
        "FulfillmentInProgress",
    )
)


def serialize_json(value: IntentState) -> str:
    return value


def deserialize_json(data: str) -> IntentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntentState value: {data!r}")
    return cast(IntentState, data)
