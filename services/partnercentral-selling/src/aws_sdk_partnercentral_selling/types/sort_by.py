"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SortBy``."""

from typing import Literal, TypeAlias, cast

SortBy: TypeAlias = Literal["CreatedDate",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SortBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SortBy:
    return cast(SortBy, data)
