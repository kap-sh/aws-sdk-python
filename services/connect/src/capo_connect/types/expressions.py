"""Generated from Smithy shape ``com.amazonaws.connect#Expressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.expression

Expressions: TypeAlias = list["capo_connect.types.expression.Expression"]


# --- restJson1 ser/de ---
def serialize_json(value: Expressions) -> list:
    import capo_connect.types.expression

    out: list = []
    for item in value:
        out.append(capo_connect.types.expression.serialize_json(item))
    return out


def deserialize_json(data: list) -> Expressions:
    import capo_connect.types.expression

    out: Expressions = []
    for item in data:
        out.append(capo_connect.types.expression.deserialize_json(item))
    return out
