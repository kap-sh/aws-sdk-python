"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliveryDestinationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination_name
    import capo_cloudwatch_logs.types.delivery_destination_policy


class PutDeliveryDestinationPolicyRequest(TypedDict, closed=True):
    delivery_destination_name: (
        "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    )
    """<p>The name of the delivery destination to assign this policy to.</p>"""
    delivery_destination_policy: "capo_cloudwatch_logs.types.delivery_destination_policy.DeliveryDestinationPolicy"
    """<p>The contents of the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliveryDestinationPolicyRequest) -> dict:
    out: dict = {}
    out["deliveryDestinationName"] = value["delivery_destination_name"]
    out["deliveryDestinationPolicy"] = value["delivery_destination_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliveryDestinationPolicyRequest:
    out: PutDeliveryDestinationPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("deliveryDestinationName") is not None:
        out["delivery_destination_name"] = data["deliveryDestinationName"]
    else:
        raise DeserializationError(
            "PutDeliveryDestinationPolicyRequest.delivery_destination_name required"
        )
    if data.get("deliveryDestinationPolicy") is not None:
        out["delivery_destination_policy"] = data["deliveryDestinationPolicy"]
    else:
        raise DeserializationError(
            "PutDeliveryDestinationPolicyRequest.delivery_destination_policy required"
        )
    return out
