"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotLocaleStatus: TypeAlias = Literal[
    "Creating",
    "Building",
    "Built",
    "ReadyExpressTesting",
    "Failed",
    "Deleting",
    "NotBuilt",
    "Importing",
    "Processing",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Building",
        "Built",
        "ReadyExpressTesting",
        "Failed",
        "Deleting",
        "NotBuilt",
        "Importing",
        "Processing",
    )
)


def serialize_json(value: BotLocaleStatus) -> str:
    return value


def deserialize_json(data: str) -> BotLocaleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotLocaleStatus value: {data!r}")
    return cast(BotLocaleStatus, data)
