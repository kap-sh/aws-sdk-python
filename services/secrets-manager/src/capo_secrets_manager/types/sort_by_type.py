"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SortByType``."""

from typing import Literal, TypeAlias, cast

SortByType: TypeAlias = Literal[
    "created-date",
    "last-accessed-date",
    "last-changed-date",
    "name",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortByType:
    return cast(SortByType, data)
