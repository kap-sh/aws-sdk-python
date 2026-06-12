"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobEarlyStoppingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrainingJobEarlyStoppingType: TypeAlias = Literal[
    "Off",
    "Auto",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Off",
        "Auto",
    )
)


def serialize_aws_json_1_1(value: TrainingJobEarlyStoppingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingJobEarlyStoppingType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrainingJobEarlyStoppingType value: {data!r}"
        )
    return cast(TrainingJobEarlyStoppingType, data)
