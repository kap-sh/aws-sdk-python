"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryConditionExpression``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.query_condition

QueryConditionExpression: TypeAlias = list[
    "aws_sdk_qconnect.types.query_condition.QueryCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryConditionExpression) -> list:
    import aws_sdk_qconnect.types.query_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.query_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryConditionExpression:
    import aws_sdk_qconnect.types.query_condition

    out: QueryConditionExpression = []
    for item in data:
        out.append(aws_sdk_qconnect.types.query_condition.deserialize_json(item))
    return out
