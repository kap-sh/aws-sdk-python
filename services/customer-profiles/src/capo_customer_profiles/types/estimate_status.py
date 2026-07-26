"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EstimateStatus``."""

from typing import Literal, TypeAlias, cast

EstimateStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EstimateStatus) -> str:
    return value


def deserialize_json(data: str) -> EstimateStatus:
    return cast(EstimateStatus, data)
