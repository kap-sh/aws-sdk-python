"""Generated from Smithy shape ``com.amazonaws.personalize#TrainingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

TrainingType: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "MANUAL",
    )
)


def serialize_aws_json_1_1(value: TrainingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingType value: {data!r}")
    return cast(TrainingType, data)
