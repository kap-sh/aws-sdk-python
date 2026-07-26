"""Generated from Smithy shape ``com.amazonaws.datasync#FilterType``."""

from typing import Literal, TypeAlias, cast

FilterType: TypeAlias = Literal["SIMPLE_PATTERN",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterType:
    return cast(FilterType, data)
