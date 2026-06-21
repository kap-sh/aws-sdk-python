"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ExpirationCriterion``."""

from typing import Literal, TypeAlias, cast

ExpirationCriterion: TypeAlias = Literal[
    "CREATED_TIMESTAMP",
    "LAST_MESSAGE_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExpirationCriterion) -> str:
    return value


def deserialize_json(data: str) -> ExpirationCriterion:
    return cast(ExpirationCriterion, data)
