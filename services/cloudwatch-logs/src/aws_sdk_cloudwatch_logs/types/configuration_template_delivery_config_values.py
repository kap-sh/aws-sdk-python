"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ConfigurationTemplateDeliveryConfigValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.field_delimiter
    import aws_sdk_cloudwatch_logs.types.record_fields
    import aws_sdk_cloudwatch_logs.types.s3_delivery_configuration


class ConfigurationTemplateDeliveryConfigValues(TypedDict):
    record_fields: NotRequired[
        "aws_sdk_cloudwatch_logs.types.record_fields.RecordFields"
    ]
    r"""<p>The default record fields that will be delivered when a list of record fields is not provided in a <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html\">CreateDelivery</a> operation.</p>"""
    field_delimiter: NotRequired[
        "aws_sdk_cloudwatch_logs.types.field_delimiter.FieldDelimiter"
    ]
    r"""<p>The default field delimiter that is used in a <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html\">CreateDelivery</a> operation when the field delimiter is not specified in that operation. The field delimiter is used only when the final output delivery is in <code>Plain</code>, <code>W3C</code>, or <code>Raw</code> format.</p>"""
    s3_delivery_configuration: NotRequired[
        "aws_sdk_cloudwatch_logs.types.s3_delivery_configuration.S3DeliveryConfiguration"
    ]
    """<p>The delivery parameters that are used when you create a delivery to a delivery destination that is an S3 Bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationTemplateDeliveryConfigValues) -> dict:
    out: dict = {}
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
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationTemplateDeliveryConfigValues:
    out: ConfigurationTemplateDeliveryConfigValues = {}  # type: ignore[typeddict-item]
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
    return out
