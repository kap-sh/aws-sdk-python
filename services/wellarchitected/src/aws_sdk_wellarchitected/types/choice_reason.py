"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ChoiceReason: TypeAlias = Literal[
    "OUT_OF_SCOPE",
    "BUSINESS_PRIORITIES",
    "ARCHITECTURE_CONSTRAINTS",
    "OTHER",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OUT_OF_SCOPE",
        "BUSINESS_PRIORITIES",
        "ARCHITECTURE_CONSTRAINTS",
        "OTHER",
        "NONE",
    )
)


def serialize_json(value: ChoiceReason) -> str:
    return value


def deserialize_json(data: str) -> ChoiceReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChoiceReason value: {data!r}")
    return cast(ChoiceReason, data)
