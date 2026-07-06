"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.domain
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status


class DatasetGroupSummary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the dataset group.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the dataset group.</p> <p>A dataset group can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING</p> </li> </ul>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the dataset group was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the dataset group was last updated.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If creating a dataset group fails, the reason behind the failure.</p>"""
    domain: NotRequired["aws_sdk_personalize.types.domain.Domain"]
    """<p>The domain of a Domain dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetGroupSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
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
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "domain" in value:
        import aws_sdk_personalize.types.domain

        out["domain"] = aws_sdk_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetGroupSummary:
    out: DatasetGroupSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
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
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "domain" in data:
        import aws_sdk_personalize.types.domain

        out["domain"] = aws_sdk_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out
