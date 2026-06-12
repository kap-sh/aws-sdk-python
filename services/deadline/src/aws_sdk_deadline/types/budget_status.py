"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

BudgetStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: BudgetStatus) -> str:
    return value


def deserialize_json(data: str) -> BudgetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BudgetStatus value: {data!r}")
    return cast(BudgetStatus, data)
