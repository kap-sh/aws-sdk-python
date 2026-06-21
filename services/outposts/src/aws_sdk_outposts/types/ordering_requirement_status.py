"""Generated from Smithy shape ``com.amazonaws.outposts#OrderingRequirementStatus``."""

from typing import Literal, TypeAlias, cast

OrderingRequirementStatus: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "EXEMPT",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderingRequirementStatus) -> str:
    return value


def deserialize_json(data: str) -> OrderingRequirementStatus:
    return cast(OrderingRequirementStatus, data)
