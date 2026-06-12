"""Generated from Smithy shape ``com.amazonaws.comprehend#ModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

ModelStatus: TypeAlias = Literal[
    "SUBMITTED",
    "TRAINING",
    "DELETING",
    "STOP_REQUESTED",
    "STOPPED",
    "IN_ERROR",
    "TRAINED",
    "TRAINED_WITH_WARNING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "TRAINING",
        "DELETING",
        "STOP_REQUESTED",
        "STOPPED",
        "IN_ERROR",
        "TRAINED",
        "TRAINED_WITH_WARNING",
    )
)


def serialize_aws_json_1_1(value: ModelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelStatus value: {data!r}")
    return cast(ModelStatus, data)
