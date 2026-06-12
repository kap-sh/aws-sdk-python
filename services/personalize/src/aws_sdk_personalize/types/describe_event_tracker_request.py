"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeEventTrackerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeEventTrackerRequest(TypedDict):
    event_tracker_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the event tracker to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventTrackerRequest) -> dict:
    out: dict = {}
    out["eventTrackerArn"] = value["event_tracker_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventTrackerRequest:
    out: DescribeEventTrackerRequest = {}  # type: ignore[typeddict-item]
    if "eventTrackerArn" in data:
        out["event_tracker_arn"] = data["eventTrackerArn"]
    else:
        raise DeserializationError(
            "DescribeEventTrackerRequest.event_tracker_arn required"
        )
    return out
