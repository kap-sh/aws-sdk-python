"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliveryDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn


class DeliveryDestinationConfiguration(TypedDict, closed=True):
    destination_resource_arn: "aws_sdk_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the Amazon Web Services destination that this delivery destination represents. That Amazon Web Services destination can be a log group in CloudWatch Logs, an Amazon S3 bucket, or a delivery stream in Firehose.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryDestinationConfiguration) -> dict:
    out: dict = {}
    out["destinationResourceArn"] = value["destination_resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryDestinationConfiguration:
    out: DeliveryDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "destinationResourceArn" in data:
        out["destination_resource_arn"] = data["destinationResourceArn"]
    else:
        raise DeserializationError(
            "DeliveryDestinationConfiguration.destination_resource_arn required"
        )
    return out
