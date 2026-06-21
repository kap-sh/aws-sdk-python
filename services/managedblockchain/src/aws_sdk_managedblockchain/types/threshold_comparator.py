"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ThresholdComparator``."""

from typing import Literal, TypeAlias, cast

ThresholdComparator: TypeAlias = Literal[
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThresholdComparator) -> str:
    return value


def deserialize_json(data: str) -> ThresholdComparator:
    return cast(ThresholdComparator, data)
