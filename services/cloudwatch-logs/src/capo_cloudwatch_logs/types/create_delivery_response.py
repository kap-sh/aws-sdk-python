"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateDeliveryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery


class CreateDeliveryResponse(TypedDict, closed=True):
    delivery: NotRequired["capo_cloudwatch_logs.types.delivery.Delivery"]
    """<p>A structure that contains information about the delivery that you just created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeliveryResponse) -> dict:
    out: dict = {}
    if "delivery" in value:
        import capo_cloudwatch_logs.types.delivery

        out["delivery"] = capo_cloudwatch_logs.types.delivery.serialize_aws_json_1_1(
            value["delivery"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeliveryResponse:
    out: CreateDeliveryResponse = {}  # type: ignore[typeddict-item]
    if "delivery" in data:
        import capo_cloudwatch_logs.types.delivery

        out["delivery"] = capo_cloudwatch_logs.types.delivery.deserialize_aws_json_1_1(
            data["delivery"]
        )
    return out
