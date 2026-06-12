"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliveryDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_destination_configuration
    import aws_sdk_cloudwatch_logs.types.delivery_destination_name
    import aws_sdk_cloudwatch_logs.types.delivery_destination_type
    import aws_sdk_cloudwatch_logs.types.output_format
    import aws_sdk_cloudwatch_logs.types.tags


class PutDeliveryDestinationRequest(TypedDict):
    name: "aws_sdk_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    """<p>A name for this delivery destination. This name must be unique for all delivery destinations in your account.</p>"""
    output_format: NotRequired[
        "aws_sdk_cloudwatch_logs.types.output_format.OutputFormat"
    ]
    """<p>The format for the logs that this delivery destination will receive.</p>"""
    delivery_destination_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination_configuration.DeliveryDestinationConfiguration"
    ]
    """<p>A structure that contains the ARN of the Amazon Web Services resource that will receive the logs.</p> <note> <p> <code>deliveryDestinationConfiguration</code> is required for CloudWatch Logs, Amazon S3, Firehose log delivery destinations and not required for X-Ray trace delivery destinations. <code>deliveryDestinationType</code> is needed for X-Ray trace delivery destinations but not required for other logs delivery destinations.</p> </note>"""
    delivery_destination_type: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination_type.DeliveryDestinationType"
    ]
    """<p>The type of delivery destination. This parameter specifies the target service where log data will be delivered. Valid values include:</p> <ul> <li> <p> <code>S3</code> - Amazon S3 for long-term storage and analytics</p> </li> <li> <p> <code>CWL</code> - CloudWatch Logs for centralized log management</p> </li> <li> <p> <code>FH</code> - Amazon Kinesis Data Firehose for real-time data streaming</p> </li> <li> <p> <code>XRAY</code> - Amazon Web Services X-Ray for distributed tracing and application monitoring</p> </li> </ul> <p>The delivery destination type determines the format and configuration options available for log delivery.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliveryDestinationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "output_format" in value:
        import aws_sdk_cloudwatch_logs.types.output_format

        out["outputFormat"] = (
            aws_sdk_cloudwatch_logs.types.output_format.serialize_aws_json_1_1(
                value["output_format"]
            )
        )
    if "delivery_destination_configuration" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_configuration

        out["deliveryDestinationConfiguration"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_configuration.serialize_aws_json_1_1(
                value["delivery_destination_configuration"]
            )
        )
    if "delivery_destination_type" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_type

        out["deliveryDestinationType"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.serialize_aws_json_1_1(
                value["delivery_destination_type"]
            )
        )
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliveryDestinationRequest:
    out: PutDeliveryDestinationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutDeliveryDestinationRequest.name required")
    if "outputFormat" in data:
        import aws_sdk_cloudwatch_logs.types.output_format

        out["output_format"] = (
            aws_sdk_cloudwatch_logs.types.output_format.deserialize_aws_json_1_1(
                data["outputFormat"]
            )
        )
    if "deliveryDestinationConfiguration" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_configuration

        out["delivery_destination_configuration"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_configuration.deserialize_aws_json_1_1(
                data["deliveryDestinationConfiguration"]
            )
        )
    if "deliveryDestinationType" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_type

        out["delivery_destination_type"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.deserialize_aws_json_1_1(
                data["deliveryDestinationType"]
            )
        )
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
