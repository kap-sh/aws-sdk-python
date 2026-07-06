"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DiscoverInputSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.parsed_input_records
    import aws_sdk_kinesis_analytics.types.processed_input_records
    import aws_sdk_kinesis_analytics.types.raw_input_records
    import aws_sdk_kinesis_analytics.types.source_schema


class DiscoverInputSchemaResponse(TypedDict, closed=True):
    input_schema: NotRequired[
        "aws_sdk_kinesis_analytics.types.source_schema.SourceSchema"
    ]
    """<p>Schema inferred from the streaming source. It identifies the format of the data in the streaming source and how each data element maps to corresponding columns in the in-application stream that you can create.</p>"""
    parsed_input_records: NotRequired[
        "aws_sdk_kinesis_analytics.types.parsed_input_records.ParsedInputRecords"
    ]
    """<p>An array of elements, where each element corresponds to a row in a stream record (a stream record can have more than one row).</p>"""
    processed_input_records: NotRequired[
        "aws_sdk_kinesis_analytics.types.processed_input_records.ProcessedInputRecords"
    ]
    """<p>Stream data that was modified by the processor specified in the <code>InputProcessingConfiguration</code> parameter.</p>"""
    raw_input_records: NotRequired[
        "aws_sdk_kinesis_analytics.types.raw_input_records.RawInputRecords"
    ]
    """<p>Raw stream data that was sampled to infer the schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverInputSchemaResponse) -> dict:
    out: dict = {}
    if "input_schema" in value:
        import aws_sdk_kinesis_analytics.types.source_schema

        out["InputSchema"] = (
            aws_sdk_kinesis_analytics.types.source_schema.serialize_aws_json_1_1(
                value["input_schema"]
            )
        )
    if "parsed_input_records" in value:
        import aws_sdk_kinesis_analytics.types.parsed_input_records

        out["ParsedInputRecords"] = (
            aws_sdk_kinesis_analytics.types.parsed_input_records.serialize_aws_json_1_1(
                value["parsed_input_records"]
            )
        )
    if "processed_input_records" in value:
        import aws_sdk_kinesis_analytics.types.processed_input_records

        out["ProcessedInputRecords"] = (
            aws_sdk_kinesis_analytics.types.processed_input_records.serialize_aws_json_1_1(
                value["processed_input_records"]
            )
        )
    if "raw_input_records" in value:
        import aws_sdk_kinesis_analytics.types.raw_input_records

        out["RawInputRecords"] = (
            aws_sdk_kinesis_analytics.types.raw_input_records.serialize_aws_json_1_1(
                value["raw_input_records"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverInputSchemaResponse:
    out: DiscoverInputSchemaResponse = {}  # type: ignore[typeddict-item]
    if "InputSchema" in data:
        import aws_sdk_kinesis_analytics.types.source_schema

        out["input_schema"] = (
            aws_sdk_kinesis_analytics.types.source_schema.deserialize_aws_json_1_1(
                data["InputSchema"]
            )
        )
    if "ParsedInputRecords" in data:
        import aws_sdk_kinesis_analytics.types.parsed_input_records

        out["parsed_input_records"] = (
            aws_sdk_kinesis_analytics.types.parsed_input_records.deserialize_aws_json_1_1(
                data["ParsedInputRecords"]
            )
        )
    if "ProcessedInputRecords" in data:
        import aws_sdk_kinesis_analytics.types.processed_input_records

        out["processed_input_records"] = (
            aws_sdk_kinesis_analytics.types.processed_input_records.deserialize_aws_json_1_1(
                data["ProcessedInputRecords"]
            )
        )
    if "RawInputRecords" in data:
        import aws_sdk_kinesis_analytics.types.raw_input_records

        out["raw_input_records"] = (
            aws_sdk_kinesis_analytics.types.raw_input_records.deserialize_aws_json_1_1(
                data["RawInputRecords"]
            )
        )
    return out
