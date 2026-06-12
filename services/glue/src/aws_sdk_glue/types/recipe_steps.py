"""Generated from Smithy shape ``com.amazonaws.glue#RecipeSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.recipe_step

RecipeSteps: TypeAlias = list["aws_sdk_glue.types.recipe_step.RecipeStep"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecipeSteps) -> list:
    import aws_sdk_glue.types.recipe_step

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.recipe_step.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecipeSteps:
    import aws_sdk_glue.types.recipe_step

    out: RecipeSteps = []
    for item in data:
        out.append(aws_sdk_glue.types.recipe_step.deserialize_aws_json_1_1(item))
    return out
