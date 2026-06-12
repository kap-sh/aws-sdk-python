"""Generated from Smithy shape ``com.amazonaws.personalize#Dataset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.dataset_type
    import aws_sdk_personalize.types.dataset_update_summary
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status
    import aws_sdk_personalize.types.tracking_id


class Dataset(TypedDict):
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the dataset.</p>"""
    dataset_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset that you want metadata for.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group.</p>"""
    dataset_type: NotRequired["aws_sdk_personalize.types.dataset_type.DatasetType"]
    """<p>One of the following values:</p> <ul> <li> <p>Interactions</p> </li> <li> <p>Items</p> </li> <li> <p>Users</p> </li> <li> <p>Actions</p> </li> <li> <p>Action_Interactions</p> </li> </ul>"""
    schema_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the associated schema.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the dataset.</p> <p>A dataset can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the dataset.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>A time stamp that shows when the dataset was updated.</p>"""
    latest_dataset_update: NotRequired[
        "aws_sdk_personalize.types.dataset_update_summary.DatasetUpdateSummary"
    ]
    """<p>Describes the latest update to the dataset.</p>"""
    tracking_id: NotRequired["aws_sdk_personalize.types.tracking_id.TrackingId"]
    """<p>The ID of the event tracker for an Action interactions dataset. You specify the tracker's ID in the <code>PutActionInteractions</code> API operation. Amazon Personalize uses it to direct new data to the Action interactions dataset in your dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Dataset) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "dataset_type" in value:
        out["datasetType"] = value["dataset_type"]
    if "schema_arn" in value:
        out["schemaArn"] = value["schema_arn"]
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
    if "latest_dataset_update" in value:
        import aws_sdk_personalize.types.dataset_update_summary

        out["latestDatasetUpdate"] = (
            aws_sdk_personalize.types.dataset_update_summary.serialize_aws_json_1_1(
                value["latest_dataset_update"]
            )
        )
    if "tracking_id" in value:
        out["trackingId"] = value["tracking_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Dataset:
    out: Dataset = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "datasetType" in data:
        out["dataset_type"] = data["datasetType"]
    if "schemaArn" in data:
        out["schema_arn"] = data["schemaArn"]
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
    if "latestDatasetUpdate" in data:
        import aws_sdk_personalize.types.dataset_update_summary

        out["latest_dataset_update"] = (
            aws_sdk_personalize.types.dataset_update_summary.deserialize_aws_json_1_1(
                data["latestDatasetUpdate"]
            )
        )
    if "trackingId" in data:
        out["tracking_id"] = data["trackingId"]
    return out
