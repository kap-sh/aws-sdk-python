"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobSortByOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HyperParameterTuningJobSortByOptions: TypeAlias = Literal[
    "Name",
    "Status",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "Status",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: HyperParameterTuningJobSortByOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobSortByOptions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HyperParameterTuningJobSortByOptions value: {data!r}"
        )
    return cast(HyperParameterTuningJobSortByOptions, data)
