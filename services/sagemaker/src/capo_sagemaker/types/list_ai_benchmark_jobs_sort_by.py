"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIBenchmarkJobsSortBy``."""

from typing import Literal, TypeAlias, cast

ListAIBenchmarkJobsSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAIBenchmarkJobsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListAIBenchmarkJobsSortBy:
    return cast(ListAIBenchmarkJobsSortBy, data)
