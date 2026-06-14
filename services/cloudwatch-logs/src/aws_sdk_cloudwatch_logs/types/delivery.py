"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Delivery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.delivery_destination_type
    import aws_sdk_cloudwatch_logs.types.delivery_id
    import aws_sdk_cloudwatch_logs.types.delivery_source_name
    import aws_sdk_cloudwatch_logs.types.field_delimiter
    import aws_sdk_cloudwatch_logs.types.record_fields
    import aws_sdk_cloudwatch_logs.types.s3_delivery_configuration
    import aws_sdk_cloudwatch_logs.types.tags


class Delivery(TypedDict):
    id: NotRequired["aws_sdk_cloudwatch_logs.types.delivery_id.DeliveryId"]
    """<p>The unique ID that identifies this delivery in your account.</p>"""
    arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies this delivery.</p>"""
    delivery_source_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_source_name.DeliverySourceName"
    ]
    """<p>The name of the delivery source that is associated with this delivery.</p>"""
    delivery_destination_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the delivery destination that is associated with this delivery.</p>"""
    delivery_destination_type: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destination_type.DeliveryDestinationType"
    ]
    """<p>Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, Firehose, or X-Ray.</p>"""
    record_fields: NotRequired[
        "aws_sdk_cloudwatch_logs.types.record_fields.RecordFields"
    ]
    """<p>The record fields used in this delivery.</p>"""
    field_delimiter: NotRequired[
        "aws_sdk_cloudwatch_logs.types.field_delimiter.FieldDelimiter"
    ]
    """<p>The field delimiter that is used between record fields when the final output format of a delivery is in <code>Plain</code>, <code>W3C</code>, or <code>Raw</code> format.</p>"""
    s3_delivery_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.s3_delivery_configuration.S3DeliveryConfiguration"
    ]
    """<p>This structure contains delivery configurations that apply only when the delivery destination resource is an S3 bucket.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>The tags that have been assigned to this delivery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Delivery) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "delivery_source_name" in value:
        out["deliverySourceName"] = value["delivery_source_name"]
    if "delivery_destination_arn" in value:
        out["deliveryDestinationArn"] = value["delivery_destination_arn"]
    if "delivery_destination_type" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_type

        out["deliveryDestinationType"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.serialize_aws_json_1_1(
                value["delivery_destination_type"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> Delivery:
    out: Delivery = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "deliverySourceName" in data:
        out["delivery_source_name"] = data["deliverySourceName"]
    if "deliveryDestinationArn" in data:
        out["delivery_destination_arn"] = data["deliveryDestinationArn"]
    if "deliveryDestinationType" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_destination_type

        out["delivery_destination_type"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.deserialize_aws_json_1_1(
                data["deliveryDestinationType"]
            )
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
