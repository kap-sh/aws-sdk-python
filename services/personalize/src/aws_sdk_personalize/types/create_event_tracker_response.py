"""Generated from Smithy shape ``com.amazonaws.personalize#CreateEventTrackerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.tracking_id


class CreateEventTrackerResponse(TypedDict, closed=True):
    event_tracker_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the event tracker.</p>"""
    tracking_id: NotRequired["aws_sdk_personalize.types.tracking_id.TrackingId"]
    r"""<p>The ID of the event tracker. Include this ID in requests to the <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html\">PutEvents</a> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventTrackerResponse) -> dict:
    out: dict = {}
    if "event_tracker_arn" in value:
        out["eventTrackerArn"] = value["event_tracker_arn"]
    if "tracking_id" in value:
        out["trackingId"] = value["tracking_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventTrackerResponse:
    out: CreateEventTrackerResponse = {}  # type: ignore[typeddict-item]
    if "eventTrackerArn" in data:
        out["event_tracker_arn"] = data["eventTrackerArn"]
    if "trackingId" in data:
        out["tracking_id"] = data["trackingId"]
    return out
