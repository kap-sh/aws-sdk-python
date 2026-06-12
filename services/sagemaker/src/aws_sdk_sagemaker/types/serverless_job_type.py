"""Generated from Smithy shape ``com.amazonaws.sagemaker#ServerlessJobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ServerlessJobType: TypeAlias = Literal[
    "FineTuning",
    "Evaluation",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FineTuning",
        "Evaluation",
    )
)


def serialize_aws_json_1_1(value: ServerlessJobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServerlessJobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServerlessJobType value: {data!r}")
    return cast(ServerlessJobType, data)
