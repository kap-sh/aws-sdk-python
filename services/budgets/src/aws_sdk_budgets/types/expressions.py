"""Generated from Smithy shape ``com.amazonaws.budgets#Expressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_budgets.types.expression

Expressions: TypeAlias = list["aws_sdk_budgets.types.expression.Expression"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Expressions) -> list:
    import aws_sdk_budgets.types.expression

    out: list = []
    for item in value:
        out.append(aws_sdk_budgets.types.expression.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Expressions:
    import aws_sdk_budgets.types.expression

    out: Expressions = []
    for item in data:
        out.append(aws_sdk_budgets.types.expression.deserialize_aws_json_1_1(item))
    return out
