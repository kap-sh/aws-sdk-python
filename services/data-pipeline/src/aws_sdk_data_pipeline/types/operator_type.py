"""Generated from Smithy shape ``com.amazonaws.datapipeline#OperatorType``."""

from typing import Literal, TypeAlias, cast

OperatorType: TypeAlias = Literal[
    "EQ",
    "REF_EQ",
    "LE",
    "GE",
    "BETWEEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatorType:
    return cast(OperatorType, data)
