"""Generated from Smithy shape ``com.amazonaws.glue#RecipeStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.condition_expression_list
    import aws_sdk_glue.types.recipe_action


class RecipeStep(TypedDict, closed=True):
    action: "aws_sdk_glue.types.recipe_action.RecipeAction"
    """<p>The transformation action of the recipe step.</p>"""
    condition_expressions: NotRequired[
        "aws_sdk_glue.types.condition_expression_list.ConditionExpressionList"
    ]
    """<p>The condition expressions for the recipe step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecipeStep) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.recipe_action

    out["Action"] = aws_sdk_glue.types.recipe_action.serialize_aws_json_1_1(
        value["action"]
    )
    if "condition_expressions" in value:
        import aws_sdk_glue.types.condition_expression_list

        out["ConditionExpressions"] = (
            aws_sdk_glue.types.condition_expression_list.serialize_aws_json_1_1(
                value["condition_expressions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecipeStep:
    out: RecipeStep = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_glue.types.recipe_action

        out["action"] = aws_sdk_glue.types.recipe_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("RecipeStep.action required")
    if "ConditionExpressions" in data:
        import aws_sdk_glue.types.condition_expression_list

        out["condition_expressions"] = (
            aws_sdk_glue.types.condition_expression_list.deserialize_aws_json_1_1(
                data["ConditionExpressions"]
            )
        )
    return out
