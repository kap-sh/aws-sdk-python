"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribePartnerEventSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_source_name


class DescribePartnerEventSourceRequest(TypedDict):
    name: "aws_sdk_eventbridge.types.event_source_name.EventSourceName"
    """<p>The name of the event source to display.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePartnerEventSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePartnerEventSourceRequest:
    out: DescribePartnerEventSourceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribePartnerEventSourceRequest.name required")
    return out
