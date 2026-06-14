"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliveryDestinationPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_destination_name
    import aws_sdk_cloudwatch_logs.types.delivery_destination_policy


class PutDeliveryDestinationPolicyRequest(TypedDict):
    delivery_destination_name: "aws_sdk_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    """<p>The name of the delivery destination to assign this policy to.</p>"""
    delivery_destination_policy: "aws_sdk_cloudwatch_logs.types.delivery_destination_policy.DeliveryDestinationPolicy"
    """<p>The contents of the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliveryDestinationPolicyRequest) -> dict:
    out: dict = {}
    out["deliveryDestinationName"] = value["delivery_destination_name"]
    out["deliveryDestinationPolicy"] = value["delivery_destination_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliveryDestinationPolicyRequest:
    out: PutDeliveryDestinationPolicyRequest = {}  # type: ignore[typeddict-item]
    if "deliveryDestinationName" in data:
        out["delivery_destination_name"] = data["deliveryDestinationName"]
    else:
        raise DeserializationError(
            "PutDeliveryDestinationPolicyRequest.delivery_destination_name required"
        )
    if "deliveryDestinationPolicy" in data:
        out["delivery_destination_policy"] = data["deliveryDestinationPolicy"]
    else:
        raise DeserializationError(
            "PutDeliveryDestinationPolicyRequest.delivery_destination_policy required"
        )
    return out
