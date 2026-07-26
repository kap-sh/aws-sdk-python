"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDeliverySourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_source


class GetDeliverySourceResponse(TypedDict, closed=True):
    delivery_source: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source.DeliverySource"
    ]
    """<p>A structure containing information about the delivery source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeliverySourceResponse) -> dict:
    out: dict = {}
    if "delivery_source" in value:
        import capo_cloudwatch_logs.types.delivery_source

        out["deliverySource"] = (
            capo_cloudwatch_logs.types.delivery_source.serialize_aws_json_1_1(
                value["delivery_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeliverySourceResponse:
    out: GetDeliverySourceResponse = {}  # type: ignore[typeddict-item]
    if "deliverySource" in data:
        import capo_cloudwatch_logs.types.delivery_source

        out["delivery_source"] = (
            capo_cloudwatch_logs.types.delivery_source.deserialize_aws_json_1_1(
                data["deliverySource"]
            )
        )
    return out
