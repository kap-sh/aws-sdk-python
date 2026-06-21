"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QueryStateInput``."""

from typing import Literal, TypeAlias, cast

QueryStateInput: TypeAlias = Literal[
    "ALL",
    "RUNNING",
    "WAITING",
    "CANCELLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryStateInput) -> str:
    return value


def deserialize_json(data: str) -> QueryStateInput:
    return cast(QueryStateInput, data)
