"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateDeliveryConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_id
    import aws_sdk_cloudwatch_logs.types.field_delimiter
    import aws_sdk_cloudwatch_logs.types.record_fields
    import aws_sdk_cloudwatch_logs.types.s3_delivery_configuration


class UpdateDeliveryConfigurationRequest(TypedDict, closed=True):
    id: "aws_sdk_cloudwatch_logs.types.delivery_id.DeliveryId"
    """<p>The ID of the delivery to be updated by this request.</p>"""
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDeliveryConfigurationRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateDeliveryConfigurationRequest:
    out: UpdateDeliveryConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateDeliveryConfigurationRequest.id required")
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
