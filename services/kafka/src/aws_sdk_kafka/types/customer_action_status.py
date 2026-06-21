"""Generated from Smithy shape ``com.amazonaws.kafka#CustomerActionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>A type of an action required from the customer.</p>"""
CustomerActionStatus: TypeAlias = Literal[
    "CRITICAL_ACTION_REQUIRED",
    "ACTION_RECOMMENDED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerActionStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomerActionStatus:
    return cast(CustomerActionStatus, data)
