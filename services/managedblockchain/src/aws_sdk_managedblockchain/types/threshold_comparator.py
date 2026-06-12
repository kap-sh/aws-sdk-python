"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ThresholdComparator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

ThresholdComparator: TypeAlias = Literal[
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL_TO",
    )
)


def serialize_json(value: ThresholdComparator) -> str:
    return value


def deserialize_json(data: str) -> ThresholdComparator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThresholdComparator value: {data!r}")
    return cast(ThresholdComparator, data)
