"""Generated from Smithy shape ``com.amazonaws.glue#FilterValueType``."""

from typing import Literal, TypeAlias, cast

FilterValueType: TypeAlias = Literal[
    "COLUMNEXTRACTED",
    "CONSTANT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterValueType:
    return cast(FilterValueType, data)
