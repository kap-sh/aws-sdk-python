"""Generated from Smithy shape ``com.amazonaws.ssm#CommandFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

CommandFilterKey: TypeAlias = Literal[
    "InvokedAfter",
    "InvokedBefore",
    "Status",
    "ExecutionStage",
    "DocumentName",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvokedAfter",
        "InvokedBefore",
        "Status",
        "ExecutionStage",
        "DocumentName",
    )
)


def serialize_aws_json_1_1(value: CommandFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandFilterKey value: {data!r}")
    return cast(CommandFilterKey, data)
