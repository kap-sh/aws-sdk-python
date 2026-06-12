"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputSchemaUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.record_columns
    import aws_sdk_kinesis_analytics_v2.types.record_encoding
    import aws_sdk_kinesis_analytics_v2.types.record_format


class InputSchemaUpdate(TypedDict):
    record_format_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.record_format.RecordFormat"
    ]
    """<p>Specifies the format of the records on the streaming source.</p>"""
    record_encoding_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.record_encoding.RecordEncoding"
    ]
    """<p>Specifies the encoding of the records in the streaming source; for example, UTF-8.</p>"""
    record_column_updates: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.record_columns.RecordColumns"
    ]
    """<p>A list of <code>RecordColumn</code> objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputSchemaUpdate) -> dict:
    out: dict = {}
    if "record_format_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.record_format

        out["RecordFormatUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.record_format.serialize_aws_json_1_1(
                value["record_format_update"]
            )
        )
    if "record_encoding_update" in value:
        out["RecordEncodingUpdate"] = value["record_encoding_update"]
    if "record_column_updates" in value:
        import aws_sdk_kinesis_analytics_v2.types.record_columns

        out["RecordColumnUpdates"] = (
            aws_sdk_kinesis_analytics_v2.types.record_columns.serialize_aws_json_1_1(
                value["record_column_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputSchemaUpdate:
    out: InputSchemaUpdate = {}  # type: ignore[typeddict-item]
    if "RecordFormatUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.record_format

        out["record_format_update"] = (
            aws_sdk_kinesis_analytics_v2.types.record_format.deserialize_aws_json_1_1(
                data["RecordFormatUpdate"]
            )
        )
    if "RecordEncodingUpdate" in data:
        out["record_encoding_update"] = data["RecordEncodingUpdate"]
    if "RecordColumnUpdates" in data:
        import aws_sdk_kinesis_analytics_v2.types.record_columns

        out["record_column_updates"] = (
            aws_sdk_kinesis_analytics_v2.types.record_columns.deserialize_aws_json_1_1(
                data["RecordColumnUpdates"]
            )
        )
    return out
