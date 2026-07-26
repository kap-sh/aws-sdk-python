"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortExperimentsBy``."""

from typing import Literal, TypeAlias, cast

SortExperimentsBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortExperimentsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortExperimentsBy:
    return cast(SortExperimentsBy, data)
