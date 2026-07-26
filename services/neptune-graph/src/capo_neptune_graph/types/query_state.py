"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QueryState``."""

from typing import Literal, TypeAlias, cast

QueryState: TypeAlias = Literal[
    "RUNNING",
    "WAITING",
    "CANCELLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryState) -> str:
    return value


def deserialize_json(data: str) -> QueryState:
    return cast(QueryState, data)
