"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliveryDestinationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_destination


class PutDeliveryDestinationResponse(TypedDict):
    delivery_destination: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination.DeliveryDestination"
    ]
    """<p>A structure containing information about the delivery destination that you just created or updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliveryDestinationResponse) -> dict:
    out: dict = {}
    if "delivery_destination" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_destination

        out["deliveryDestination"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination.serialize_aws_json_1_1(
                value["delivery_destination"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliveryDestinationResponse:
    out: PutDeliveryDestinationResponse = {}  # type: ignore[typeddict-item]
    if "deliveryDestination" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_destination

        out["delivery_destination"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination.deserialize_aws_json_1_1(
                data["deliveryDestination"]
            )
        )
    return out
