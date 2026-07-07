"""Generated from Smithy shape ``com.amazonaws.personalize#AutoMLResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class AutoMLResult(TypedDict, closed=True):
    best_recipe_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the best recipe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLResult) -> dict:
    out: dict = {}
    if "best_recipe_arn" in value:
        out["bestRecipeArn"] = value["best_recipe_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLResult:
    out: AutoMLResult = {}  # type: ignore[typeddict-item]
    if "bestRecipeArn" in data:
        out["best_recipe_arn"] = data["bestRecipeArn"]
    return out
