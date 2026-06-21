"""Generated from Smithy shape ``com.amazonaws.lakeformation#QueryStateString``."""

from typing import Literal, TypeAlias, cast

QueryStateString: TypeAlias = Literal[
    "PENDING",
    "WORKUNITS_AVAILABLE",
    "ERROR",
    "FINISHED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryStateString) -> str:
    return value


def deserialize_json(data: str) -> QueryStateString:
    return cast(QueryStateString, data)
