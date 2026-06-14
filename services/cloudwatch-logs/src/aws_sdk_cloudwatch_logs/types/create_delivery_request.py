"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateDeliveryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.delivery_source_name
    import aws_sdk_cloudwatch_logs.types.field_delimiter
    import aws_sdk_cloudwatch_logs.types.record_fields
    import aws_sdk_cloudwatch_logs.types.s3_delivery_configuration
    import aws_sdk_cloudwatch_logs.types.tags


class CreateDeliveryRequest(TypedDict):
    delivery_source_name: (
        "aws_sdk_cloudwatch_logs.types.delivery_source_name.DeliverySourceName"
    )
    """<p>The name of the delivery source to use for this delivery.</p>"""
    delivery_destination_arn: "aws_sdk_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the delivery destination to use for this delivery.</p>"""
    record_fields: NotRequired[
        "aws_sdk_cloudwatch_logs.types.record_fields.RecordFields"
    ]
    """<p>The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.</p>"""
    field_delimiter: NotRequired[
        "aws_sdk_cloudwatch_logs.types.field_delimiter.FieldDelimiter"
    ]
    """<p>The field delimiter to use between record fields when the final output format of a delivery is in <code>Plain</code>, <code>W3C</code>, or <code>Raw</code> format.</p>"""
    s3_delivery_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.s3_delivery_configuration.S3DeliveryConfiguration"
    ]
    """<p>This structure contains parameters that are valid only when the delivery's delivery destination is an S3 bucket.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeliveryRequest) -> dict:
    out: dict = {}
    out["deliverySourceName"] = value["delivery_source_name"]
    out["deliveryDestinationArn"] = value["delivery_destination_arn"]
    if "record_fields" in value:
        import aws_sdk_cloudwatch_logs.types.record_fields

        out["recordFields"] = (
            aws_sdk_cloudwatch_logs.types.record_fields.serialize_aws_json_1_1(
                value["record_fields"]
            )
        )
    if "field_delimiter" in value:
        out["fieldDelimiter"] = value["field_delimiter"]
    if "s3_delivery_configuration" in value:
        import aws_sdk_cloudwatch_logs.types.s3_delivery_configuration

        out["s3DeliveryConfiguration"] = (
            aws_sdk_cloudwatch_logs.types.s3_delivery_configuration.serialize_aws_json_1_1(
                value["s3_delivery_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeliveryRequest:
    out: CreateDeliveryRequest = {}  # type: ignore[typeddict-item]
    if "deliverySourceName" in data:
        out["delivery_source_name"] = data["deliverySourceName"]
    else:
        raise DeserializationError(
            "CreateDeliveryRequest.delivery_source_name required"
        )
    if "deliveryDestinationArn" in data:
        out["delivery_destination_arn"] = data["deliveryDestinationArn"]
    else:
        raise DeserializationError(
            "CreateDeliveryRequest.delivery_destination_arn required"
        )
    if "recordFields" in data:
        import aws_sdk_cloudwatch_logs.types.record_fields

        out["record_fields"] = (
            aws_sdk_cloudwatch_logs.types.record_fields.deserialize_aws_json_1_1(
                data["recordFields"]
            )
        )
    if "fieldDelimiter" in data:
        out["field_delimiter"] = data["fieldDelimiter"]
    if "s3DeliveryConfiguration" in data:
        import aws_sdk_cloudwatch_logs.types.s3_delivery_configuration

        out["s3_delivery_configuration"] = (
            aws_sdk_cloudwatch_logs.types.s3_delivery_configuration.deserialize_aws_json_1_1(
                data["s3DeliveryConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
