"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Policy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_destination_policy


class Policy(TypedDict):
    delivery_destination_policy: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination_policy.DeliveryDestinationPolicy"
    ]
    """<p>The contents of the delivery destination policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Policy) -> dict:
    out: dict = {}
    if "delivery_destination_policy" in value:
        out["deliveryDestinationPolicy"] = value["delivery_destination_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Policy:
    out: Policy = {}  # type: ignore[typeddict-item]
    if "deliveryDestinationPolicy" in data:
        out["delivery_destination_policy"] = data["deliveryDestinationPolicy"]
    return out
