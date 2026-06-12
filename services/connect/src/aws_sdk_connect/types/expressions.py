"""Generated from Smithy shape ``com.amazonaws.connect#Expressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.expression

Expressions: TypeAlias = list["aws_sdk_connect.types.expression.Expression"]


# --- restJson1 ser/de ---
def serialize_json(value: Expressions) -> list:
    import aws_sdk_connect.types.expression

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.expression.serialize_json(item))
    return out


def deserialize_json(data: list) -> Expressions:
    import aws_sdk_connect.types.expression

    out: Expressions = []
    for item in data:
        out.append(aws_sdk_connect.types.expression.deserialize_json(item))
    return out
