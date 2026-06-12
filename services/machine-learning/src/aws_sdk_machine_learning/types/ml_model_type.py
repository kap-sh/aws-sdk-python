"""Generated from Smithy shape ``com.amazonaws.machinelearning#MLModelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_machine_learning.errors import DeserializationError

MLModelType: TypeAlias = Literal[
    "REGRESSION",
    "BINARY",
    "MULTICLASS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGRESSION",
        "BINARY",
        "MULTICLASS",
    )
)


def serialize_aws_json_1_1(value: MLModelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MLModelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MLModelType value: {data!r}")
    return cast(MLModelType, data)
