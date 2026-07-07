"""Generated from Smithy shape ``com.amazonaws.firehose#DescribeDeliveryStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_description


class DescribeDeliveryStreamOutput(TypedDict, closed=True):
    delivery_stream_description: (
        "aws_sdk_firehose.types.delivery_stream_description.DeliveryStreamDescription"
    )
    """<p>Information about the Firehose stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryStreamOutput) -> dict:
    out: dict = {}
    import aws_sdk_firehose.types.delivery_stream_description

    out["DeliveryStreamDescription"] = (
        aws_sdk_firehose.types.delivery_stream_description.serialize_aws_json_1_1(
            value["delivery_stream_description"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryStreamOutput:
    out: DescribeDeliveryStreamOutput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamDescription" in data:
        import aws_sdk_firehose.types.delivery_stream_description

        out["delivery_stream_description"] = (
            aws_sdk_firehose.types.delivery_stream_description.deserialize_aws_json_1_1(
                data["DeliveryStreamDescription"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDeliveryStreamOutput.delivery_stream_description required"
        )
    return out
