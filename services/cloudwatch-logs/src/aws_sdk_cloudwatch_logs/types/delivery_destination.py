"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliveryDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.delivery_destination_configuration
    import aws_sdk_cloudwatch_logs.types.delivery_destination_name
    import aws_sdk_cloudwatch_logs.types.delivery_destination_type
    import aws_sdk_cloudwatch_logs.types.output_format
    import aws_sdk_cloudwatch_logs.types.tags


class DeliveryDestination(TypedDict):
    name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    ]
    """<p>The name of this delivery destination.</p>"""
    arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.</p>"""
    delivery_destination_type: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination_type.DeliveryDestinationType"
    ]
    """<p>Displays whether this delivery destination is CloudWatch Logs, Amazon S3, Firehose, or X-Ray.</p>"""
    output_format: NotRequired[
        "aws_sdk_cloudwatch_logs.types.output_format.OutputFormat"
    ]
    """<p>The format of the logs that are sent to this delivery destination. </p>"""
    delivery_destination_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination_configuration.DeliveryDestinationConfiguration"
    ]
    """<p>A structure that contains the ARN of the Amazon Web Services resource that will receive the logs.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>The tags that have been assigned to this delivery destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryDestination) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "delivery_destination_type" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_type

        out["deliveryDestinationType"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.serialize_aws_json_1_1(
                value["delivery_destination_type"]
            )
        )
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
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryDestination:
    out: DeliveryDestination = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "deliveryDestinationType" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_type

        out["delivery_destination_type"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.deserialize_aws_json_1_1(
                data["deliveryDestinationType"]
            )
        )
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
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
