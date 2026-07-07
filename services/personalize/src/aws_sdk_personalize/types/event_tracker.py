"""Generated from Smithy shape ``com.amazonaws.personalize#EventTracker``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.account_id
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status
    import aws_sdk_personalize.types.tracking_id


class EventTracker(TypedDict, closed=True):
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the event tracker.</p>"""
    event_tracker_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the event tracker.</p>"""
    account_id: NotRequired["aws_sdk_personalize.types.account_id.AccountId"]
    """<p>The Amazon Web Services account that owns the event tracker.</p>"""
    tracking_id: NotRequired["aws_sdk_personalize.types.tracking_id.TrackingId"]
    r"""<p>The ID of the event tracker. Include this ID in requests to the <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html\">PutEvents</a> API.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group that receives the event data.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the event tracker.</p> <p>An event tracker can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the event tracker was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the event tracker was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTracker) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "event_tracker_arn" in value:
        out["eventTrackerArn"] = value["event_tracker_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "tracking_id" in value:
        out["trackingId"] = value["tracking_id"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> EventTracker:
    out: EventTracker = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "eventTrackerArn" in data:
        out["event_tracker_arn"] = data["eventTrackerArn"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "trackingId" in data:
        out["tracking_id"] = data["trackingId"]
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
    return out
