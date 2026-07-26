"""Generated from Smithy shape ``com.amazonaws.quicksight#MaximumMinimumComputationType``."""

from typing import Literal, TypeAlias, cast

MaximumMinimumComputationType: TypeAlias = Literal[
    "MAXIMUM",
    "MINIMUM",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaximumMinimumComputationType) -> str:
    return value


def deserialize_json(data: str) -> MaximumMinimumComputationType:
    return cast(MaximumMinimumComputationType, data)
