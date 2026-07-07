"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#SourceSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.record_columns
    import aws_sdk_kinesis_analytics.types.record_encoding
    import aws_sdk_kinesis_analytics.types.record_format


class SourceSchema(TypedDict, closed=True):
    record_format: "aws_sdk_kinesis_analytics.types.record_format.RecordFormat"
    """<p>Specifies the format of the records on the streaming source.</p>"""
    record_encoding: NotRequired[
        "aws_sdk_kinesis_analytics.types.record_encoding.RecordEncoding"
    ]
    """<p>Specifies the encoding of the records in the streaming source. For example, UTF-8.</p>"""
    record_columns: "aws_sdk_kinesis_analytics.types.record_columns.RecordColumns"
    """<p>A list of <code>RecordColumn</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceSchema) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics.types.record_format

    out["RecordFormat"] = (
        aws_sdk_kinesis_analytics.types.record_format.serialize_aws_json_1_1(
            value["record_format"]
        )
    )
    if "record_encoding" in value:
        out["RecordEncoding"] = value["record_encoding"]
    import aws_sdk_kinesis_analytics.types.record_columns

    out["RecordColumns"] = (
        aws_sdk_kinesis_analytics.types.record_columns.serialize_aws_json_1_1(
            value["record_columns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceSchema:
    out: SourceSchema = {}  # type: ignore[typeddict-item]
    if "RecordFormat" in data:
        import aws_sdk_kinesis_analytics.types.record_format

        out["record_format"] = (
            aws_sdk_kinesis_analytics.types.record_format.deserialize_aws_json_1_1(
                data["RecordFormat"]
            )
        )
    else:
        raise DeserializationError("SourceSchema.record_format required")
    if "RecordEncoding" in data:
        out["record_encoding"] = data["RecordEncoding"]
    if "RecordColumns" in data:
        import aws_sdk_kinesis_analytics.types.record_columns

        out["record_columns"] = (
            aws_sdk_kinesis_analytics.types.record_columns.deserialize_aws_json_1_1(
                data["RecordColumns"]
            )
        )
    else:
        raise DeserializationError("SourceSchema.record_columns required")
    return out
