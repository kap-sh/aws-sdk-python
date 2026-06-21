"""Generated from Smithy shape ``com.amazonaws.codecommit#SortByEnum``."""

from typing import Literal, TypeAlias, cast

SortByEnum: TypeAlias = Literal[
    "repositoryName",
    "lastModifiedDate",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortByEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortByEnum:
    return cast(SortByEnum, data)
