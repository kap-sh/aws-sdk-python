"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ExecutionType: TypeAlias = Literal[
    "STANDARD",
    "ROLLBACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "ROLLBACK",
    )
)


def serialize_aws_json_1_1(value: ExecutionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionType value: {data!r}")
    return cast(ExecutionType, data)
