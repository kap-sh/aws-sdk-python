"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#FailureHandlingPolicy``."""

from typing import Literal, TypeAlias, cast

FailureHandlingPolicy: TypeAlias = Literal[
    "ROLLBACK_ON_FAILURE",
    "DO_NOTHING",
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureHandlingPolicy) -> str:
    return value


def deserialize_json(data: str) -> FailureHandlingPolicy:
    return cast(FailureHandlingPolicy, data)
