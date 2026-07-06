"""Generated from Smithy shape ``com.amazonaws.personalize#DeleteEventTrackerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DeleteEventTrackerRequest(TypedDict, closed=True):
    event_tracker_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the event tracker to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventTrackerRequest) -> dict:
    out: dict = {}
    out["eventTrackerArn"] = value["event_tracker_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventTrackerRequest:
    out: DeleteEventTrackerRequest = {}  # type: ignore[typeddict-item]
    if "eventTrackerArn" in data:
        out["event_tracker_arn"] = data["eventTrackerArn"]
    else:
        raise DeserializationError(
            "DeleteEventTrackerRequest.event_tracker_arn required"
        )
    return out
