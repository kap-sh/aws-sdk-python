"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionRedriveStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

ExecutionRedriveStatus: TypeAlias = Literal[
    "REDRIVABLE",
    "NOT_REDRIVABLE",
    "REDRIVABLE_BY_MAP_RUN",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REDRIVABLE",
        "NOT_REDRIVABLE",
        "REDRIVABLE_BY_MAP_RUN",
    )
)


def serialize_aws_json_1_0(value: ExecutionRedriveStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionRedriveStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionRedriveStatus value: {data!r}")
    return cast(ExecutionRedriveStatus, data)
