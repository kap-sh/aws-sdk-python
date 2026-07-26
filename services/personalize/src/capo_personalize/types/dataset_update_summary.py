"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetUpdateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.status


class DatasetUpdateSummary(TypedDict, closed=True):
    schema_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the schema that replaced the previous schema of the dataset.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the dataset update. </p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If updating a dataset fails, provides the reason why.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the dataset update.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The last update date and time (in Unix time) of the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetUpdateSummary) -> dict:
    out: dict = {}
    if "schema_arn" in value:
        out["schemaArn"] = value["schema_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetUpdateSummary:
    out: DatasetUpdateSummary = {}  # type: ignore[typeddict-item]
    if "schemaArn" in data:
        out["schema_arn"] = data["schemaArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
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
    return out
