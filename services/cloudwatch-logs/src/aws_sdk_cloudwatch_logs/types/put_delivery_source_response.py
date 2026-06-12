"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliverySourceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_source


class PutDeliverySourceResponse(TypedDict):
    delivery_source: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_source.DeliverySource"
    ]
    """<p>A structure containing information about the delivery source that was just created or updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliverySourceResponse) -> dict:
    out: dict = {}
    if "delivery_source" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_source

        out["deliverySource"] = (
            aws_sdk_cloudwatch_logs.types.delivery_source.serialize_aws_json_1_1(
                value["delivery_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliverySourceResponse:
    out: PutDeliverySourceResponse = {}  # type: ignore[typeddict-item]
    if "deliverySource" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_source

        out["delivery_source"] = (
            aws_sdk_cloudwatch_logs.types.delivery_source.deserialize_aws_json_1_1(
                data["deliverySource"]
            )
        )
    return out
