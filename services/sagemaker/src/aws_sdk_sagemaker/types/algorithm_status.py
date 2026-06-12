"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AlgorithmStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Completed",
        "Failed",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: AlgorithmStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlgorithmStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlgorithmStatus value: {data!r}")
    return cast(AlgorithmStatus, data)
