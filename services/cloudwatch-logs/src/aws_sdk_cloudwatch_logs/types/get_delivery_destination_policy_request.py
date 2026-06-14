"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDeliveryDestinationPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_destination_name


class GetDeliveryDestinationPolicyRequest(TypedDict):
    delivery_destination_name: "aws_sdk_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    """<p>The name of the delivery destination that you want to retrieve the policy of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeliveryDestinationPolicyRequest) -> dict:
    out: dict = {}
    out["deliveryDestinationName"] = value["delivery_destination_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeliveryDestinationPolicyRequest:
    out: GetDeliveryDestinationPolicyRequest = {}  # type: ignore[typeddict-item]
    if "deliveryDestinationName" in data:
        out["delivery_destination_name"] = data["deliveryDestinationName"]
    else:
        raise DeserializationError(
            "GetDeliveryDestinationPolicyRequest.delivery_destination_name required"
        )
    return out
