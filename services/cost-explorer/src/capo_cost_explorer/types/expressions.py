"""Generated from Smithy shape ``com.amazonaws.costexplorer#Expressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.expression

Expressions: TypeAlias = list["capo_cost_explorer.types.expression.Expression"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Expressions) -> list:
    import capo_cost_explorer.types.expression

    out: list = []
    for item in value:
        out.append(capo_cost_explorer.types.expression.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Expressions:
    import capo_cost_explorer.types.expression

    out: Expressions = []
    for item in data:
        out.append(capo_cost_explorer.types.expression.deserialize_aws_json_1_1(item))
    return out
