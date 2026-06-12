"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExecutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InferenceExecutionMode: TypeAlias = Literal[
    "Serial",
    "Direct",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Serial",
        "Direct",
    )
)


def serialize_aws_json_1_1(value: InferenceExecutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceExecutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceExecutionMode value: {data!r}")
    return cast(InferenceExecutionMode, data)
