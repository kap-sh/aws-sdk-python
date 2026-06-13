"""Generated from Smithy shape ``com.amazonaws.backup#RuleExecutionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

RuleExecutionType: TypeAlias = Literal[
    "CONTINUOUS",
    "SNAPSHOTS",
    "CONTINUOUS_AND_SNAPSHOTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUOUS",
        "SNAPSHOTS",
        "CONTINUOUS_AND_SNAPSHOTS",
    )
)


def serialize_json(value: RuleExecutionType) -> str:
    return value


def deserialize_json(data: str) -> RuleExecutionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleExecutionType value: {data!r}")
    return cast(RuleExecutionType, data)
