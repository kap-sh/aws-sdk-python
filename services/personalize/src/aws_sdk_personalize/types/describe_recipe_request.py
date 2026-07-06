"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeRecipeRequest(TypedDict, closed=True):
    recipe_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recipe to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRecipeRequest) -> dict:
    out: dict = {}
    out["recipeArn"] = value["recipe_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRecipeRequest:
    out: DescribeRecipeRequest = {}  # type: ignore[typeddict-item]
    if "recipeArn" in data:
        out["recipe_arn"] = data["recipeArn"]
    else:
        raise DeserializationError("DescribeRecipeRequest.recipe_arn required")
    return out
