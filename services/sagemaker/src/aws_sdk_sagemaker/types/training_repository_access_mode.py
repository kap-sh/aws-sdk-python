"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingRepositoryAccessMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrainingRepositoryAccessMode: TypeAlias = Literal[
    "Platform",
    "Vpc",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Platform",
        "Vpc",
    )
)


def serialize_aws_json_1_1(value: TrainingRepositoryAccessMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingRepositoryAccessMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrainingRepositoryAccessMode value: {data!r}"
        )
    return cast(TrainingRepositoryAccessMode, data)
