"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionRedriveFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

ExecutionRedriveFilter: TypeAlias = Literal[
    "REDRIVEN",
    "NOT_REDRIVEN",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REDRIVEN",
        "NOT_REDRIVEN",
    )
)


def serialize_aws_json_1_0(value: ExecutionRedriveFilter) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionRedriveFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionRedriveFilter value: {data!r}")
    return cast(ExecutionRedriveFilter, data)
