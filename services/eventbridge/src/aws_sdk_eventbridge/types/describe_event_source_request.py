"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeEventSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_source_name


class DescribeEventSourceRequest(TypedDict):
    name: "aws_sdk_eventbridge.types.event_source_name.EventSourceName"
    """<p>The name of the partner event source to display the details of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventSourceRequest:
    out: DescribeEventSourceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeEventSourceRequest.name required")
    return out
