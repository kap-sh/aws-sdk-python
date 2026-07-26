"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Policy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination_policy


class Policy(TypedDict, closed=True):
    delivery_destination_policy: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination_policy.DeliveryDestinationPolicy"
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
