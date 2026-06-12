"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteDeliveryDestinationPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_destination_name


class DeleteDeliveryDestinationPolicyRequest(TypedDict):
    delivery_destination_name: "aws_sdk_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    """<p>The name of the delivery destination that you want to delete the policy for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeliveryDestinationPolicyRequest) -> dict:
    out: dict = {}
    out["deliveryDestinationName"] = value["delivery_destination_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeliveryDestinationPolicyRequest:
    out: DeleteDeliveryDestinationPolicyRequest = {}  # type: ignore[typeddict-item]
    if "deliveryDestinationName" in data:
        out["delivery_destination_name"] = data["deliveryDestinationName"]
    else:
        raise DeserializationError(
            "DeleteDeliveryDestinationPolicyRequest.delivery_destination_name required"
        )
    return out
