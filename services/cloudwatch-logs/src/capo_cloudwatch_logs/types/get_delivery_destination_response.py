"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDeliveryDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination


class GetDeliveryDestinationResponse(TypedDict, closed=True):
    delivery_destination: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination.DeliveryDestination"
    ]
    """<p>A structure containing information about the delivery destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeliveryDestinationResponse) -> dict:
    out: dict = {}
    if "delivery_destination" in value:
        import capo_cloudwatch_logs.types.delivery_destination

        out["deliveryDestination"] = (
            capo_cloudwatch_logs.types.delivery_destination.serialize_aws_json_1_1(
                value["delivery_destination"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeliveryDestinationResponse:
    out: GetDeliveryDestinationResponse = {}  # type: ignore[typeddict-item]
    if data.get("deliveryDestination") is not None:
        import capo_cloudwatch_logs.types.delivery_destination

        out["delivery_destination"] = (
            capo_cloudwatch_logs.types.delivery_destination.deserialize_aws_json_1_1(
                data["deliveryDestination"]
            )
        )
    return out
