"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TraversalType``."""

from typing import Literal, TypeAlias, cast

TraversalType: TypeAlias = Literal["PATH_TO_ROOT",]


# --- restJson1 ser/de ---
def serialize_json(value: TraversalType) -> str:
    return value


def deserialize_json(data: str) -> TraversalType:
    return cast(TraversalType, data)
