"""Generated from Smithy shape ``com.amazonaws.personalize#RecipeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.domain
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status


class RecipeSummary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the recipe.</p>"""
    recipe_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recipe.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the recipe.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the recipe was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the recipe was last updated.</p>"""
    domain: NotRequired["aws_sdk_personalize.types.domain.Domain"]
    """<p>The domain of the recipe (if the recipe is a Domain dataset group use case).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecipeSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date_time" in value:
        import aws_sdk_personalize.types.date

        out["creationDateTime"] = aws_sdk_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_personalize.types.date

        out["lastUpdatedDateTime"] = (
            aws_sdk_personalize.types.date.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "domain" in value:
        import aws_sdk_personalize.types.domain

        out["domain"] = aws_sdk_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecipeSummary:
    out: RecipeSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "recipeArn" in data:
        out["recipe_arn"] = data["recipeArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "creationDateTime" in data:
        import aws_sdk_personalize.types.date

        out["creation_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_personalize.types.date

        out["last_updated_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "domain" in data:
        import aws_sdk_personalize.types.domain

        out["domain"] = aws_sdk_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out
