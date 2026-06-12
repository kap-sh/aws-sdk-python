"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ExecutionMode: TypeAlias = Literal[
    "QUEUED",
    "SUPERSEDED",
    "PARALLEL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "SUPERSEDED",
        "PARALLEL",
    )
)


def serialize_aws_json_1_1(value: ExecutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionMode value: {data!r}")
    return cast(ExecutionMode, data)
