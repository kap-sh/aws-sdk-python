"""Generated from Smithy shape ``com.amazonaws.devopsagent#OrderType``."""

from typing import Literal, TypeAlias, cast

"""<p>Sort order options for journal operations</p>"""
OrderType: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderType) -> str:
    return value


def deserialize_json(data: str) -> OrderType:
    return cast(OrderType, data)
