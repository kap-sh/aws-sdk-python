"""Generated from Smithy shape ``com.amazonaws.frauddetector#TrainingDataSourceEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

TrainingDataSourceEnum: TypeAlias = Literal[
    "EXTERNAL_EVENTS",
    "INGESTED_EVENTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXTERNAL_EVENTS",
        "INGESTED_EVENTS",
    )
)


def serialize_aws_json_1_1(value: TrainingDataSourceEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingDataSourceEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingDataSourceEnum value: {data!r}")
    return cast(TrainingDataSourceEnum, data)
