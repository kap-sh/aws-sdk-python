"""Generated from Smithy shape ``com.amazonaws.personalize#TrainingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

TrainingMode: TypeAlias = Literal[
    "FULL",
    "UPDATE",
    "AUTOTRAIN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "UPDATE",
        "AUTOTRAIN",
    )
)


def serialize_aws_json_1_1(value: TrainingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingMode value: {data!r}")
    return cast(TrainingMode, data)
