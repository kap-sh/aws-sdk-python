"""Generated from Smithy shape ``com.amazonaws.personalize#Recipe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.description
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.recipe_type
    import aws_sdk_personalize.types.status


class Recipe(TypedDict, closed=True):
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the recipe.</p>"""
    recipe_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recipe.</p>"""
    algorithm_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the algorithm that Amazon Personalize uses to train the model.</p>"""
    feature_transformation_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the FeatureTransformation object.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the recipe.</p>"""
    description: NotRequired["aws_sdk_personalize.types.description.Description"]
    """<p>The description of the recipe.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the recipe was created.</p>"""
    recipe_type: NotRequired["aws_sdk_personalize.types.recipe_type.RecipeType"]
    """<p>One of the following values:</p> <ul> <li> <p>PERSONALIZED_RANKING</p> </li> <li> <p>RELATED_ITEMS</p> </li> <li> <p>USER_PERSONALIZATION</p> </li> </ul>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the recipe was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recipe) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
    if "algorithm_arn" in value:
        out["algorithmArn"] = value["algorithm_arn"]
    if "feature_transformation_arn" in value:
        out["featureTransformationArn"] = value["feature_transformation_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_date_time" in value:
        import aws_sdk_personalize.types.date

        out["creationDateTime"] = aws_sdk_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "recipe_type" in value:
        out["recipeType"] = value["recipe_type"]
    if "last_updated_date_time" in value:
        import aws_sdk_personalize.types.date

        out["lastUpdatedDateTime"] = (
            aws_sdk_personalize.types.date.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Recipe:
    out: Recipe = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "recipeArn" in data:
        out["recipe_arn"] = data["recipeArn"]
    if "algorithmArn" in data:
        out["algorithm_arn"] = data["algorithmArn"]
    if "featureTransformationArn" in data:
        out["feature_transformation_arn"] = data["featureTransformationArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationDateTime" in data:
        import aws_sdk_personalize.types.date

        out["creation_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "recipeType" in data:
        out["recipe_type"] = data["recipeType"]
    if "lastUpdatedDateTime" in data:
        import aws_sdk_personalize.types.date

        out["last_updated_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    return out
