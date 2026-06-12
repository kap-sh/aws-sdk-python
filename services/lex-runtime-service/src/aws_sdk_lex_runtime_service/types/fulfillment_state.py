"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#FulfillmentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_service.errors import DeserializationError

FulfillmentState: TypeAlias = Literal[
    "Fulfilled",
    "Failed",
    "ReadyForFulfillment",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Fulfilled",
        "Failed",
        "ReadyForFulfillment",
    )
)


def serialize_json(value: FulfillmentState) -> str:
    return value


def deserialize_json(data: str) -> FulfillmentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FulfillmentState value: {data!r}")
    return cast(FulfillmentState, data)
