"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ChoiceStatus: TypeAlias = Literal[
    "SELECTED",
    "NOT_APPLICABLE",
    "UNSELECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELECTED",
        "NOT_APPLICABLE",
        "UNSELECTED",
    )
)


def serialize_json(value: ChoiceStatus) -> str:
    return value


def deserialize_json(data: str) -> ChoiceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChoiceStatus value: {data!r}")
    return cast(ChoiceStatus, data)
