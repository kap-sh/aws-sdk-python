"""Generated from Smithy shape ``com.amazonaws.personalize#SolutionUpdateSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.perform_auto_training
    import aws_sdk_personalize.types.perform_incremental_update
    import aws_sdk_personalize.types.solution_update_config
    import aws_sdk_personalize.types.status


class SolutionUpdateSummary(TypedDict):
    solution_update_config: NotRequired[
        "aws_sdk_personalize.types.solution_update_config.SolutionUpdateConfig"
    ]
    """<p>The configuration details of the solution.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the solution update. A solution update can be in one of the following states:</p> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p>"""
    perform_auto_training: NotRequired[
        "aws_sdk_personalize.types.perform_auto_training.PerformAutoTraining"
    ]
    """<p>Whether the solution automatically creates solution versions.</p>"""
    perform_incremental_update: NotRequired[
        "aws_sdk_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
    ]
    """<p>A Boolean value that indicates whether incremental training updates are performed on the model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the solution update was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the solution update was last updated.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If a solution update fails, the reason behind the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SolutionUpdateSummary) -> dict:
    out: dict = {}
    if "solution_update_config" in value:
        import aws_sdk_personalize.types.solution_update_config

        out["solutionUpdateConfig"] = (
            aws_sdk_personalize.types.solution_update_config.serialize_aws_json_1_1(
                value["solution_update_config"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "perform_auto_training" in value:
        out["performAutoTraining"] = value["perform_auto_training"]
    if "perform_incremental_update" in value:
        out["performIncrementalUpdate"] = value["perform_incremental_update"]
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
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SolutionUpdateSummary:
    out: SolutionUpdateSummary = {}  # type: ignore[typeddict-item]
    if "solutionUpdateConfig" in data:
        import aws_sdk_personalize.types.solution_update_config

        out["solution_update_config"] = (
            aws_sdk_personalize.types.solution_update_config.deserialize_aws_json_1_1(
                data["solutionUpdateConfig"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "performAutoTraining" in data:
        out["perform_auto_training"] = data["performAutoTraining"]
    if "performIncrementalUpdate" in data:
        out["perform_incremental_update"] = data["performIncrementalUpdate"]
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
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
