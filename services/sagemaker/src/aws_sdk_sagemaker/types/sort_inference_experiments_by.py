"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortInferenceExperimentsBy``."""

from typing import Literal, TypeAlias, cast

SortInferenceExperimentsBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortInferenceExperimentsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortInferenceExperimentsBy:
    return cast(SortInferenceExperimentsBy, data)
