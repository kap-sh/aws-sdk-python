"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobSortByOptions``."""

from typing import Literal, TypeAlias, cast

HyperParameterTuningJobSortByOptions: TypeAlias = Literal[
    "Name",
    "Status",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobSortByOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobSortByOptions:
    return cast(HyperParameterTuningJobSortByOptions, data)
