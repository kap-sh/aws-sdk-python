"""Generated from Smithy shape ``com.amazonaws.glue#FieldFilterOperator``."""

from typing import Literal, TypeAlias, cast

FieldFilterOperator: TypeAlias = Literal[
    "LESS_THAN",
    "GREATER_THAN",
    "BETWEEN",
    "EQUAL_TO",
    "NOT_EQUAL_TO",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN_OR_EQUAL_TO",
    "CONTAINS",
    "ORDER_BY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FieldFilterOperator:
    return cast(FieldFilterOperator, data)
