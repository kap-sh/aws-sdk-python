"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KinesisFirehoseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class KinesisFirehoseInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the delivery stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisFirehoseInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisFirehoseInput:
    out: KinesisFirehoseInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("KinesisFirehoseInput.resource_arn required")
    return out
