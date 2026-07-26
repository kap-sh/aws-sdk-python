"""Generated from Smithy shape ``com.amazonaws.personalize#SolutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.name
    import capo_personalize.types.status


class SolutionSummary(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the solution.</p>"""
    solution_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the solution.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the solution.</p> <p>A solution can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the solution was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the solution was last updated.</p>"""
    recipe_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recipe used by the solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SolutionSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "solution_arn" in value:
        out["solutionArn"] = value["solution_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SolutionSummary:
    out: SolutionSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "solutionArn" in data:
        out["solution_arn"] = data["solutionArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "creationDateTime" in data:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "recipeArn" in data:
        out["recipe_arn"] = data["recipeArn"]
    return out
