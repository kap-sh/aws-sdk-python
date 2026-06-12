"""Generated from Smithy shape ``com.amazonaws.personalize#BatchInferenceJobMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

BatchInferenceJobMode: TypeAlias = Literal[
    "BATCH_INFERENCE",
    "THEME_GENERATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BATCH_INFERENCE",
        "THEME_GENERATION",
    )
)


def serialize_aws_json_1_1(value: BatchInferenceJobMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchInferenceJobMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchInferenceJobMode value: {data!r}")
    return cast(BatchInferenceJobMode, data)
