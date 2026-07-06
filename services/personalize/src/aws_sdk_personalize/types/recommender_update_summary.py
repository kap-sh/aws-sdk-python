"""Generated from Smithy shape ``com.amazonaws.personalize#RecommenderUpdateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.recommender_config
    import aws_sdk_personalize.types.status


class RecommenderUpdateSummary(TypedDict, closed=True):
    recommender_config: NotRequired[
        "aws_sdk_personalize.types.recommender_config.RecommenderConfig"
    ]
    """<p>The configuration details of the recommender update.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the recommender update was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the recommender update was last updated.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the recommender update. A recommender update can be in one of the following states:</p> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If a recommender update fails, the reason behind the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommenderUpdateSummary) -> dict:
    out: dict = {}
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
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommenderUpdateSummary:
    out: RecommenderUpdateSummary = {}  # type: ignore[typeddict-item]
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
    return out
