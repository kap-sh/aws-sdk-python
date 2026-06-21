"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FailureCategory``."""

from typing import Literal, TypeAlias, cast

FailureCategory: TypeAlias = Literal[
    "SHARED_FATE",
    "EXCESSIVE_LOAD",
    "EXCESSIVE_LATENCY",
    "MISCONFIGURATION_AND_BUGS",
    "SINGLE_POINT_OF_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureCategory) -> str:
    return value


def deserialize_json(data: str) -> FailureCategory:
    return cast(FailureCategory, data)
