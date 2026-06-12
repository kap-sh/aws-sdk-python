"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.destination_name


class DeleteDestinationRequest(TypedDict):
    destination_name: "aws_sdk_cloudwatch_logs.types.destination_name.DestinationName"
    """<p>The name of the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDestinationRequest) -> dict:
    out: dict = {}
    out["destinationName"] = value["destination_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDestinationRequest:
    out: DeleteDestinationRequest = {}  # type: ignore[typeddict-item]
    if "destinationName" in data:
        out["destination_name"] = data["destinationName"]
    else:
        raise DeserializationError("DeleteDestinationRequest.destination_name required")
    return out
