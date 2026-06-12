"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

ModelVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "TRAINING_CANCELLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "TRAINING_CANCELLED",
    )
)


def serialize_aws_json_1_1(value: ModelVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelVersionStatus value: {data!r}")
    return cast(ModelVersionStatus, data)
