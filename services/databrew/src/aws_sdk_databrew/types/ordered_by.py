"""Generated from Smithy shape ``com.amazonaws.databrew#OrderedBy``."""

from typing import Literal, TypeAlias, cast

OrderedBy: TypeAlias = Literal["LAST_MODIFIED_DATE",]


# --- restJson1 ser/de ---
def serialize_json(value: OrderedBy) -> str:
    return value


def deserialize_json(data: str) -> OrderedBy:
    return cast(OrderedBy, data)
