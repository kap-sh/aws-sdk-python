"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ConflictResolvingModel``."""

from typing import Literal, TypeAlias, cast

ConflictResolvingModel: TypeAlias = Literal[
    "RECENCY",
    "SOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictResolvingModel) -> str:
    return value


def deserialize_json(data: str) -> ConflictResolvingModel:
    return cast(ConflictResolvingModel, data)
