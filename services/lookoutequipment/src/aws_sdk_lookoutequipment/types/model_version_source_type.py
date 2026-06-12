"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelVersionSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

ModelVersionSourceType: TypeAlias = Literal[
    "TRAINING",
    "RETRAINING",
    "IMPORT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRAINING",
        "RETRAINING",
        "IMPORT",
    )
)


def serialize_aws_json_1_0(value: ModelVersionSourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelVersionSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelVersionSourceType value: {data!r}")
    return cast(ModelVersionSourceType, data)
