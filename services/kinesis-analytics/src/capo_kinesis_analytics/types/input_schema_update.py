"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputSchemaUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.record_columns
    import capo_kinesis_analytics.types.record_encoding
    import capo_kinesis_analytics.types.record_format


class InputSchemaUpdate(TypedDict, closed=True):
    record_format_update: NotRequired[
        "capo_kinesis_analytics.types.record_format.RecordFormat"
    ]
    """<p>Specifies the format of the records on the streaming source.</p>"""
    record_encoding_update: NotRequired[
        "capo_kinesis_analytics.types.record_encoding.RecordEncoding"
    ]
    """<p>Specifies the encoding of the records in the streaming source. For example, UTF-8.</p>"""
    record_column_updates: NotRequired[
        "capo_kinesis_analytics.types.record_columns.RecordColumns"
    ]
    """<p>A list of <code>RecordColumn</code> objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputSchemaUpdate) -> dict:
    out: dict = {}
    if "record_format_update" in value:
        import capo_kinesis_analytics.types.record_format

        out["RecordFormatUpdate"] = (
            capo_kinesis_analytics.types.record_format.serialize_aws_json_1_1(
                value["record_format_update"]
            )
        )
    if "record_encoding_update" in value:
        out["RecordEncodingUpdate"] = value["record_encoding_update"]
    if "record_column_updates" in value:
        import capo_kinesis_analytics.types.record_columns

        out["RecordColumnUpdates"] = (
            capo_kinesis_analytics.types.record_columns.serialize_aws_json_1_1(
                value["record_column_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputSchemaUpdate:
    out: InputSchemaUpdate = {}  # type: ignore[typeddict-item]
    if "RecordFormatUpdate" in data:
        import capo_kinesis_analytics.types.record_format

        out["record_format_update"] = (
            capo_kinesis_analytics.types.record_format.deserialize_aws_json_1_1(
                data["RecordFormatUpdate"]
            )
        )
    if "RecordEncodingUpdate" in data:
        out["record_encoding_update"] = data["RecordEncodingUpdate"]
    if "RecordColumnUpdates" in data:
        import capo_kinesis_analytics.types.record_columns

        out["record_column_updates"] = (
            capo_kinesis_analytics.types.record_columns.deserialize_aws_json_1_1(
                data["RecordColumnUpdates"]
            )
        )
    return out
