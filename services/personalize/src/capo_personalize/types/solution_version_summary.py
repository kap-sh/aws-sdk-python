"""Generated from Smithy shape ``com.amazonaws.personalize#SolutionVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.status
    import capo_personalize.types.training_mode
    import capo_personalize.types.training_type


class SolutionVersionSummary(TypedDict, closed=True):
    solution_version_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the solution version.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the solution version.</p> <p>A solution version can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> </ul>"""
    training_mode: NotRequired["capo_personalize.types.training_mode.TrainingMode"]
    """<p>The scope of training to be performed when creating the solution version. A <code>FULL</code> training considers all of the data in your dataset group. An <code>UPDATE</code> processes only the data that has changed since the latest training. Only solution versions created with the User-Personalization recipe can use <code>UPDATE</code>. </p>"""
    training_type: NotRequired["capo_personalize.types.training_type.TrainingType"]
    """<p>Whether the solution version was created automatically or manually.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that this version of a solution was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the solution version was last updated.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If a solution version fails, the reason behind the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SolutionVersionSummary) -> dict:
    out: dict = {}
    if "solution_version_arn" in value:
        out["solutionVersionArn"] = value["solution_version_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "training_mode" in value:
        import capo_personalize.types.training_mode

        out["trainingMode"] = (
            capo_personalize.types.training_mode.serialize_aws_json_1_1(
                value["training_mode"]
            )
        )
    if "training_type" in value:
        import capo_personalize.types.training_type

        out["trainingType"] = (
            capo_personalize.types.training_type.serialize_aws_json_1_1(
                value["training_type"]
            )
        )
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
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SolutionVersionSummary:
    out: SolutionVersionSummary = {}  # type: ignore[typeddict-item]
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "trainingMode" in data:
        import capo_personalize.types.training_mode

        out["training_mode"] = (
            capo_personalize.types.training_mode.deserialize_aws_json_1_1(
                data["trainingMode"]
            )
        )
    if "trainingType" in data:
        import capo_personalize.types.training_type

        out["training_type"] = (
            capo_personalize.types.training_type.deserialize_aws_json_1_1(
                data["trainingType"]
            )
        )
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
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
