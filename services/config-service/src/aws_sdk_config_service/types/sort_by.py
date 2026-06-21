"""Generated from Smithy shape ``com.amazonaws.configservice#SortBy``."""

from typing import Literal, TypeAlias, cast

SortBy: TypeAlias = Literal["SCORE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortBy:
    return cast(SortBy, data)
