"""Generated from Smithy shape ``com.amazonaws.appflow#AggregationType``."""

from typing import Literal, TypeAlias, cast

AggregationType: TypeAlias = Literal[
    "None",
    "SingleFile",
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationType) -> str:
    return value


def deserialize_json(data: str) -> AggregationType:
    return cast(AggregationType, data)
