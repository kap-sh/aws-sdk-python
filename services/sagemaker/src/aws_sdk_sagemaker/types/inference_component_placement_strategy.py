"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentPlacementStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InferenceComponentPlacementStrategy: TypeAlias = Literal[
    "SPREAD",
    "BINPACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPREAD",
        "BINPACK",
    )
)


def serialize_aws_json_1_1(value: InferenceComponentPlacementStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceComponentPlacementStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InferenceComponentPlacementStrategy value: {data!r}"
        )
    return cast(InferenceComponentPlacementStrategy, data)
