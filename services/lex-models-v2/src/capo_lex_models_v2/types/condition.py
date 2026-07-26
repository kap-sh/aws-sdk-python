"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.condition_expression


class Condition(TypedDict, closed=True):
    expression_string: (
        "capo_lex_models_v2.types.condition_expression.ConditionExpression"
    )
    """<p>The expression string that is evaluated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    out["expressionString"] = value["expression_string"]
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "expressionString" in data:
        out["expression_string"] = data["expressionString"]
    else:
        raise DeserializationError("Condition.expression_string required")
    return out
