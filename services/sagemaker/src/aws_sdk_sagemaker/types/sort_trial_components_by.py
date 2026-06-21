"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortTrialComponentsBy``."""

from typing import Literal, TypeAlias, cast

SortTrialComponentsBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortTrialComponentsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortTrialComponentsBy:
    return cast(SortTrialComponentsBy, data)
