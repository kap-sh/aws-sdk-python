"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeRecipeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.recipe


class DescribeRecipeResponse(TypedDict):
    recipe: NotRequired["aws_sdk_personalize.types.recipe.Recipe"]
    """<p>An object that describes the recipe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRecipeResponse) -> dict:
    out: dict = {}
    if "recipe" in value:
        import aws_sdk_personalize.types.recipe

        out["recipe"] = aws_sdk_personalize.types.recipe.serialize_aws_json_1_1(
            value["recipe"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRecipeResponse:
    out: DescribeRecipeResponse = {}  # type: ignore[typeddict-item]
    if "recipe" in data:
        import aws_sdk_personalize.types.recipe

        out["recipe"] = aws_sdk_personalize.types.recipe.deserialize_aws_json_1_1(
            data["recipe"]
        )
    return out
