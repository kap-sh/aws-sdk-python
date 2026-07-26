"""Generated from Smithy shape ``com.amazonaws.connect#Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attribute_condition
    import capo_connect.types.expressions


class Expression(TypedDict, closed=True):
    attribute_condition: NotRequired[
        "capo_connect.types.attribute_condition.AttributeCondition"
    ]
    """<p>An object to specify the predefined attribute condition.</p>"""
    and_expression: NotRequired["capo_connect.types.expressions.Expressions"]
    """<p>List of routing expressions which will be AND-ed together.</p>"""
    or_expression: NotRequired["capo_connect.types.expressions.Expressions"]
    """<p>List of routing expressions which will be OR-ed together.</p>"""
    not_attribute_condition: NotRequired[
        "capo_connect.types.attribute_condition.AttributeCondition"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Expression) -> dict:
    out: dict = {}
    if "attribute_condition" in value:
        import capo_connect.types.attribute_condition

        out["AttributeCondition"] = (
            capo_connect.types.attribute_condition.serialize_json(
                value["attribute_condition"]
            )
        )
    if "and_expression" in value:
        import capo_connect.types.expressions

        out["AndExpression"] = capo_connect.types.expressions.serialize_json(
            value["and_expression"]
        )
    if "or_expression" in value:
        import capo_connect.types.expressions

        out["OrExpression"] = capo_connect.types.expressions.serialize_json(
            value["or_expression"]
        )
    if "not_attribute_condition" in value:
        import capo_connect.types.attribute_condition

        out["NotAttributeCondition"] = (
            capo_connect.types.attribute_condition.serialize_json(
                value["not_attribute_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "AttributeCondition" in data:
        import capo_connect.types.attribute_condition

        out["attribute_condition"] = (
            capo_connect.types.attribute_condition.deserialize_json(
                data["AttributeCondition"]
            )
        )
    if "AndExpression" in data:
        import capo_connect.types.expressions

        out["and_expression"] = capo_connect.types.expressions.deserialize_json(
            data["AndExpression"]
        )
    if "OrExpression" in data:
        import capo_connect.types.expressions

        out["or_expression"] = capo_connect.types.expressions.deserialize_json(
            data["OrExpression"]
        )
    if "NotAttributeCondition" in data:
        import capo_connect.types.attribute_condition

        out["not_attribute_condition"] = (
            capo_connect.types.attribute_condition.deserialize_json(
                data["NotAttributeCondition"]
            )
        )
    return out
