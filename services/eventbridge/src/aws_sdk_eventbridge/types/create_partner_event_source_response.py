"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreatePartnerEventSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.string


class CreatePartnerEventSourceResponse(TypedDict, closed=True):
    event_source_arn: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>The ARN of the partner event source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartnerEventSourceResponse) -> dict:
    out: dict = {}
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartnerEventSourceResponse:
    out: CreatePartnerEventSourceResponse = {}  # type: ignore[typeddict-item]
    if "EventSourceArn" in data:
        out["event_source_arn"] = data["EventSourceArn"]
    return out
