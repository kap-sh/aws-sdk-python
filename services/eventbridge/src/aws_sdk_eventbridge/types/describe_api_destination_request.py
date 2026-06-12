"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeApiDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.api_destination_name


class DescribeApiDestinationRequest(TypedDict):
    name: "aws_sdk_eventbridge.types.api_destination_name.ApiDestinationName"
    """<p>The name of the API destination to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApiDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApiDestinationRequest:
    out: DescribeApiDestinationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeApiDestinationRequest.name required")
    return out
