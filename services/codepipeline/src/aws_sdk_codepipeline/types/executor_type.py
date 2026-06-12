"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ExecutorType: TypeAlias = Literal[
    "JobWorker",
    "Lambda",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JobWorker",
        "Lambda",
    )
)


def serialize_aws_json_1_1(value: ExecutorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutorType value: {data!r}")
    return cast(ExecutorType, data)
