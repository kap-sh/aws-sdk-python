"""Generated from Smithy shape ``com.amazonaws.personalize#Recommender``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.metrics
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.recommender_config
    import aws_sdk_personalize.types.recommender_update_summary
    import aws_sdk_personalize.types.status


class Recommender(TypedDict, closed=True):
    recommender_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recommender.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Domain dataset group that contains the recommender.</p>"""
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the recommender.</p>"""
    recipe_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recipe (Domain dataset group use case) that the recommender was created for. </p>"""
    recommender_config: NotRequired[
        "aws_sdk_personalize.types.recommender_config.RecommenderConfig"
    ]
    """<p>The configuration details of the recommender.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the recommender was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the recommender was last updated.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the recommender.</p> <p>A recommender can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>STOP PENDING > STOP IN_PROGRESS > INACTIVE > START PENDING > START IN_PROGRESS > ACTIVE</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If a recommender fails, the reason behind the failure.</p>"""
    latest_recommender_update: NotRequired[
        "aws_sdk_personalize.types.recommender_update_summary.RecommenderUpdateSummary"
    ]
    """<p>Provides a summary of the latest updates to the recommender. </p>"""
    model_metrics: NotRequired["aws_sdk_personalize.types.metrics.Metrics"]
    r"""<p>Provides evaluation metrics that help you determine the performance of a recommender. For more information, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/evaluating-recommenders.html\"> Evaluating a recommender</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recommender) -> dict:
    out: dict = {}
    if "recommender_arn" in value:
        out["recommenderArn"] = value["recommender_arn"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
    if "recommender_config" in value:
        import aws_sdk_personalize.types.recommender_config

        out["recommenderConfig"] = (
            aws_sdk_personalize.types.recommender_config.serialize_aws_json_1_1(
                value["recommender_config"]
            )
        )
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
    if "status" in value:
        out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "latest_recommender_update" in value:
        import aws_sdk_personalize.types.recommender_update_summary

        out["latestRecommenderUpdate"] = (
            aws_sdk_personalize.types.recommender_update_summary.serialize_aws_json_1_1(
                value["latest_recommender_update"]
            )
        )
    if "model_metrics" in value:
        import aws_sdk_personalize.types.metrics

        out["modelMetrics"] = aws_sdk_personalize.types.metrics.serialize_aws_json_1_1(
            value["model_metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Recommender:
    out: Recommender = {}  # type: ignore[typeddict-item]
    if "recommenderArn" in data:
        out["recommender_arn"] = data["recommenderArn"]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "recipeArn" in data:
        out["recipe_arn"] = data["recipeArn"]
    if "recommenderConfig" in data:
        import aws_sdk_personalize.types.recommender_config

        out["recommender_config"] = (
            aws_sdk_personalize.types.recommender_config.deserialize_aws_json_1_1(
                data["recommenderConfig"]
            )
        )
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
    if "status" in data:
        out["status"] = data["status"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "latestRecommenderUpdate" in data:
        import aws_sdk_personalize.types.recommender_update_summary

        out["latest_recommender_update"] = (
            aws_sdk_personalize.types.recommender_update_summary.deserialize_aws_json_1_1(
                data["latestRecommenderUpdate"]
            )
        )
    if "modelMetrics" in data:
        import aws_sdk_personalize.types.metrics

        out["model_metrics"] = (
            aws_sdk_personalize.types.metrics.deserialize_aws_json_1_1(
                data["modelMetrics"]
            )
        )
    return out
