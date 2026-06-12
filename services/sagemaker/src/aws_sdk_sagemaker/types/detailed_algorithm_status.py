"""Generated from Smithy shape ``com.amazonaws.sagemaker#DetailedAlgorithmStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

DetailedAlgorithmStatus: TypeAlias = Literal[
    "NotStarted",
    "InProgress",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotStarted",
        "InProgress",
        "Completed",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: DetailedAlgorithmStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetailedAlgorithmStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetailedAlgorithmStatus value: {data!r}")
    return cast(DetailedAlgorithmStatus, data)
