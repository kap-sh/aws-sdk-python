"""Generated from Smithy shape ``com.amazonaws.personalize#FilterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.name
    import capo_personalize.types.status


class FilterSummary(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the filter.</p>"""
    filter_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the filter.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The time at which the filter was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The time at which the filter was last updated.</p>"""
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the dataset group to which the filter belongs.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If the filter failed, the reason for the failure.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
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
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterSummary:
    out: FilterSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
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
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "status" in data:
        out["status"] = data["status"]
    return out
