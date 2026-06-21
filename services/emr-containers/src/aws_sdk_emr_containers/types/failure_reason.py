"""Generated from Smithy shape ``com.amazonaws.emrcontainers#FailureReason``."""

from typing import Literal, TypeAlias, cast

FailureReason: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "USER_ERROR",
    "VALIDATION_ERROR",
    "CLUSTER_UNAVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureReason) -> str:
    return value


def deserialize_json(data: str) -> FailureReason:
    return cast(FailureReason, data)
