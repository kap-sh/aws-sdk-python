"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.condition_expression_list
    import capo_databrew.types.recipe_action


class RecipeStep(TypedDict, closed=True):
    action: "capo_databrew.types.recipe_action.RecipeAction"
    """<p>The particular action to be performed in the recipe step.</p>"""
    condition_expressions: NotRequired[
        "capo_databrew.types.condition_expression_list.ConditionExpressionList"
    ]
    """<p>One or more conditions that must be met for the recipe step to succeed.</p> <note> <p>All of the conditions in the array must be met. In other words, all of the conditions must be combined using a logical AND operation.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecipeStep) -> dict:
    out: dict = {}
    import capo_databrew.types.recipe_action

    out["Action"] = capo_databrew.types.recipe_action.serialize_json(value["action"])
    if "condition_expressions" in value:
        import capo_databrew.types.condition_expression_list

        out["ConditionExpressions"] = (
            capo_databrew.types.condition_expression_list.serialize_json(
                value["condition_expressions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecipeStep:
    out: RecipeStep = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_databrew.types.recipe_action

        out["action"] = capo_databrew.types.recipe_action.deserialize_json(
            data["Action"]
        )
    else:
        raise DeserializationError("RecipeStep.action required")
    if "ConditionExpressions" in data:
        import capo_databrew.types.condition_expression_list

        out["condition_expressions"] = (
            capo_databrew.types.condition_expression_list.deserialize_json(
                data["ConditionExpressions"]
            )
        )
    return out
