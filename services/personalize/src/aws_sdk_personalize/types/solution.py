"""Generated from Smithy shape ``com.amazonaws.personalize#Solution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.auto_ml_result
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.event_type
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.perform_auto_ml
    import aws_sdk_personalize.types.perform_auto_training
    import aws_sdk_personalize.types.perform_hpo
    import aws_sdk_personalize.types.perform_incremental_update
    import aws_sdk_personalize.types.solution_config
    import aws_sdk_personalize.types.solution_update_summary
    import aws_sdk_personalize.types.solution_version_summary
    import aws_sdk_personalize.types.status


class Solution(TypedDict):
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the solution.</p>"""
    solution_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the solution.</p>"""
    perform_hpo: "aws_sdk_personalize.types.perform_hpo.PerformHPO"
    """<p>Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is <code>false</code>.</p>"""
    perform_auto_ml: "aws_sdk_personalize.types.perform_auto_ml.PerformAutoML"
    r"""<important> <p>We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/determining-use-case.html\">Determining your use case.</a> </p> </important> <p>When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration (<code>recipeArn</code> must not be specified). When false (the default), Amazon Personalize uses <code>recipeArn</code> for training.</p>"""
    perform_auto_training: NotRequired[
        "aws_sdk_personalize.types.perform_auto_training.PerformAutoTraining"
    ]
    r"""<p>Specifies whether the solution automatically creates solution versions. The default is <code>True</code> and the solution automatically creates new solution versions every 7 days.</p> <p>For more information about auto training, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html\">Creating and configuring a solution</a>.</p>"""
    perform_incremental_update: NotRequired[
        "aws_sdk_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
    ]
    """<p>A Boolean value that indicates whether incremental training updates are performed on the model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe</p>"""
    recipe_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the recipe used to create the solution. This is required when <code>performAutoML</code> is false.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group that provides the training data.</p>"""
    event_type: NotRequired["aws_sdk_personalize.types.event_type.EventType"]
    """<p>The event type (for example, 'click' or 'like') that is used for training the model. If no <code>eventType</code> is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.</p>"""
    solution_config: NotRequired[
        "aws_sdk_personalize.types.solution_config.SolutionConfig"
    ]
    """<p>Describes the configuration properties for the solution.</p>"""
    auto_ml_result: NotRequired["aws_sdk_personalize.types.auto_ml_result.AutoMLResult"]
    """<p>When <code>performAutoML</code> is true, specifies the best recipe found.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the solution.</p> <p>A solution can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the solution.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the solution was last updated.</p>"""
    latest_solution_version: NotRequired[
        "aws_sdk_personalize.types.solution_version_summary.SolutionVersionSummary"
    ]
    """<p>Describes the latest version of the solution, including the status and the ARN.</p>"""
    latest_solution_update: NotRequired[
        "aws_sdk_personalize.types.solution_update_summary.SolutionUpdateSummary"
    ]
    """<p>Provides a summary of the latest updates to the solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Solution) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "solution_arn" in value:
        out["solutionArn"] = value["solution_arn"]
    out["performHPO"] = value.get("perform_hpo", False)
    out["performAutoML"] = value.get("perform_auto_ml", False)
    if "perform_auto_training" in value:
        out["performAutoTraining"] = value["perform_auto_training"]
    if "perform_incremental_update" in value:
        out["performIncrementalUpdate"] = value["perform_incremental_update"]
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "event_type" in value:
        out["eventType"] = value["event_type"]
    if "solution_config" in value:
        import aws_sdk_personalize.types.solution_config

        out["solutionConfig"] = (
            aws_sdk_personalize.types.solution_config.serialize_aws_json_1_1(
                value["solution_config"]
            )
        )
    if "auto_ml_result" in value:
        import aws_sdk_personalize.types.auto_ml_result

        out["autoMLResult"] = (
            aws_sdk_personalize.types.auto_ml_result.serialize_aws_json_1_1(
                value["auto_ml_result"]
            )
        )
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
    if "latest_solution_version" in value:
        import aws_sdk_personalize.types.solution_version_summary

        out["latestSolutionVersion"] = (
            aws_sdk_personalize.types.solution_version_summary.serialize_aws_json_1_1(
                value["latest_solution_version"]
            )
        )
    if "latest_solution_update" in value:
        import aws_sdk_personalize.types.solution_update_summary

        out["latestSolutionUpdate"] = (
            aws_sdk_personalize.types.solution_update_summary.serialize_aws_json_1_1(
                value["latest_solution_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Solution:
    out: Solution = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "solutionArn" in data:
        out["solution_arn"] = data["solutionArn"]
    if "performHPO" in data:
        out["perform_hpo"] = data["performHPO"]
    else:
        out["perform_hpo"] = False
    if "performAutoML" in data:
        out["perform_auto_ml"] = data["performAutoML"]
    else:
        out["perform_auto_ml"] = False
    if "performAutoTraining" in data:
        out["perform_auto_training"] = data["performAutoTraining"]
    if "performIncrementalUpdate" in data:
        out["perform_incremental_update"] = data["performIncrementalUpdate"]
    if "recipeArn" in data:
        out["recipe_arn"] = data["recipeArn"]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    if "solutionConfig" in data:
        import aws_sdk_personalize.types.solution_config

        out["solution_config"] = (
            aws_sdk_personalize.types.solution_config.deserialize_aws_json_1_1(
                data["solutionConfig"]
            )
        )
    if "autoMLResult" in data:
        import aws_sdk_personalize.types.auto_ml_result

        out["auto_ml_result"] = (
            aws_sdk_personalize.types.auto_ml_result.deserialize_aws_json_1_1(
                data["autoMLResult"]
            )
        )
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
    if "latestSolutionVersion" in data:
        import aws_sdk_personalize.types.solution_version_summary

        out["latest_solution_version"] = (
            aws_sdk_personalize.types.solution_version_summary.deserialize_aws_json_1_1(
                data["latestSolutionVersion"]
            )
        )
    if "latestSolutionUpdate" in data:
        import aws_sdk_personalize.types.solution_update_summary

        out["latest_solution_update"] = (
            aws_sdk_personalize.types.solution_update_summary.deserialize_aws_json_1_1(
                data["latestSolutionUpdate"]
            )
        )
    return out
