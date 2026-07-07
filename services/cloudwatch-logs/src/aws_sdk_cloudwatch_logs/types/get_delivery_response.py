"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDeliveryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery


class GetDeliveryResponse(TypedDict, closed=True):
    delivery: NotRequired["aws_sdk_cloudwatch_logs.types.delivery.Delivery"]
    """<p>A structure that contains information about the delivery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeliveryResponse) -> dict:
    out: dict = {}
    if "delivery" in value:
        import aws_sdk_cloudwatch_logs.types.delivery

        out["delivery"] = aws_sdk_cloudwatch_logs.types.delivery.serialize_aws_json_1_1(
            value["delivery"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeliveryResponse:
    out: GetDeliveryResponse = {}  # type: ignore[typeddict-item]
    if "delivery" in data:
        import aws_sdk_cloudwatch_logs.types.delivery

        out["delivery"] = (
            aws_sdk_cloudwatch_logs.types.delivery.deserialize_aws_json_1_1(
                data["delivery"]
            )
        )
    return out
