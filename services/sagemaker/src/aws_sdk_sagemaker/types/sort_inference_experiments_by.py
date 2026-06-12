"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortInferenceExperimentsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortInferenceExperimentsBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: SortInferenceExperimentsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortInferenceExperimentsBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SortInferenceExperimentsBy value: {data!r}"
        )
    return cast(SortInferenceExperimentsBy, data)
