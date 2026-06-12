"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDeliverySourceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_source_name


class GetDeliverySourceRequest(TypedDict):
    name: "aws_sdk_cloudwatch_logs.types.delivery_source_name.DeliverySourceName"
    """<p>The name of the delivery source that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeliverySourceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeliverySourceRequest:
    out: GetDeliverySourceRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetDeliverySourceRequest.name required")
    return out
