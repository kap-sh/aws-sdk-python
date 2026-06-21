"""Generated from Smithy shape ``com.amazonaws.opensearch#OverallChangeStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The overall status value of the domain configuration change.</p>"""
OverallChangeStatus: TypeAlias = Literal[
    "PENDING",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OverallChangeStatus) -> str:
    return value


def deserialize_json(data: str) -> OverallChangeStatus:
    return cast(OverallChangeStatus, data)
