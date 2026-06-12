"""Generated from Smithy shape ``com.amazonaws.glue#DQTransformOutput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DQTransformOutput: TypeAlias = Literal[
    "PrimaryInput",
    "EvaluationResults",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PrimaryInput",
        "EvaluationResults",
    )
)


def serialize_aws_json_1_1(value: DQTransformOutput) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DQTransformOutput:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DQTransformOutput value: {data!r}")
    return cast(DQTransformOutput, data)
