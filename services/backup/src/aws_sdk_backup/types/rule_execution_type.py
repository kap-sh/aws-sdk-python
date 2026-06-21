"""Generated from Smithy shape ``com.amazonaws.backup#RuleExecutionType``."""

from typing import Literal, TypeAlias, cast

RuleExecutionType: TypeAlias = Literal[
    "CONTINUOUS",
    "SNAPSHOTS",
    "CONTINUOUS_AND_SNAPSHOTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleExecutionType) -> str:
    return value


def deserialize_json(data: str) -> RuleExecutionType:
    return cast(RuleExecutionType, data)
