"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDeliveryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_id


class GetDeliveryRequest(TypedDict):
    id: "aws_sdk_cloudwatch_logs.types.delivery_id.DeliveryId"
    """<p>The ID of the delivery that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeliveryRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeliveryRequest:
    out: GetDeliveryRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetDeliveryRequest.id required")
    return out
