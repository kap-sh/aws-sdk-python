"""Generated from Smithy shape ``com.amazonaws.budgets#Expressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.expression

Expressions: TypeAlias = list["capo_budgets.types.expression.Expression"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Expressions) -> list:
    import capo_budgets.types.expression

    out: list = []
    for item in value:
        out.append(capo_budgets.types.expression.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Expressions:
    import capo_budgets.types.expression

    out: Expressions = []
    for item in data:
        out.append(capo_budgets.types.expression.deserialize_aws_json_1_1(item))
    return out
