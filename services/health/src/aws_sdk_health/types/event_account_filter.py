"""Generated from Smithy shape ``com.amazonaws.health#EventAccountFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_health.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_health.types.account_id
    import aws_sdk_health.types.event_arn


class EventAccountFilter(TypedDict):
    event_arn: "aws_sdk_health.types.event_arn.eventArn"
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    aws_account_id: NotRequired["aws_sdk_health.types.account_id.accountId"]
    """<p>The 12-digit Amazon Web Services account numbers that contains the affected entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventAccountFilter) -> dict:
    out: dict = {}
    out["eventArn"] = value["event_arn"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventAccountFilter:
    out: EventAccountFilter = {}  # type: ignore[typeddict-item]
    if "eventArn" in data:
        out["event_arn"] = data["eventArn"]
    else:
        raise DeserializationError("EventAccountFilter.event_arn required")
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    return out
