"""Generated from Smithy shape ``com.amazonaws.connect#RoutingExpressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_expression

RoutingExpressions: TypeAlias = list[
    "aws_sdk_connect.types.routing_expression.RoutingExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingExpressions) -> list:
    return list(value)


def deserialize_json(data: list) -> RoutingExpressions:
    return list(data)
