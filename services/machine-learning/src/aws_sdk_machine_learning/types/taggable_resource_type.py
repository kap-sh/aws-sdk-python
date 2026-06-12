"""Generated from Smithy shape ``com.amazonaws.machinelearning#TaggableResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_machine_learning.errors import DeserializationError

TaggableResourceType: TypeAlias = Literal[
    "BatchPrediction",
    "DataSource",
    "Evaluation",
    "MLModel",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BatchPrediction",
        "DataSource",
        "Evaluation",
        "MLModel",
    )
)


def serialize_aws_json_1_1(value: TaggableResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaggableResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaggableResourceType value: {data!r}")
    return cast(TaggableResourceType, data)
