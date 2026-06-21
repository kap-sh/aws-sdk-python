"""Generated from Smithy shape ``com.amazonaws.budgets#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

"""<p> The comparison operator of a notification. Currently, the service supports the following operators:</p> <p> <code>GREATER_THAN</code>, <code>LESS_THAN</code>, <code>EQUAL_TO</code> </p>"""
ComparisonOperator: TypeAlias = Literal[
    "GREATER_THAN",
    "LESS_THAN",
    "EQUAL_TO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
