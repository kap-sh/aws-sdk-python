"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExpressionVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.expression_variable

ExpressionVariables: TypeAlias = list[
    "aws_sdk_iotsitewise.types.expression_variable.ExpressionVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExpressionVariables) -> list:
    import aws_sdk_iotsitewise.types.expression_variable

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.expression_variable.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExpressionVariables:
    import aws_sdk_iotsitewise.types.expression_variable

    out: ExpressionVariables = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.expression_variable.deserialize_json(item))
    return out
