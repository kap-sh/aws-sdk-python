"""Generated from Smithy shape ``com.amazonaws.lakeformation#Condition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.expression_string


class Condition(TypedDict):
    expression: NotRequired[
        "aws_sdk_lakeformation.types.expression_string.ExpressionString"
    ]
    """<p>An expression written based on the Cedar Policy Language used to match the principal attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    if "expression" in value:
        out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    return out
