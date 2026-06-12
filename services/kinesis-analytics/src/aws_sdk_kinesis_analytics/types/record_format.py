"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#RecordFormat``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.mapping_parameters
    import aws_sdk_kinesis_analytics.types.record_format_type


class RecordFormat(TypedDict):
    record_format_type: (
        "aws_sdk_kinesis_analytics.types.record_format_type.RecordFormatType"
    )
    """<p>The type of record format.</p>"""
    mapping_parameters: NotRequired[
        "aws_sdk_kinesis_analytics.types.mapping_parameters.MappingParameters"
    ]
    """<p>When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordFormat) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics.types.record_format_type

    out["RecordFormatType"] = (
        aws_sdk_kinesis_analytics.types.record_format_type.serialize_aws_json_1_1(
            value["record_format_type"]
        )
    )
    if "mapping_parameters" in value:
        import aws_sdk_kinesis_analytics.types.mapping_parameters

        out["MappingParameters"] = (
            aws_sdk_kinesis_analytics.types.mapping_parameters.serialize_aws_json_1_1(
                value["mapping_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordFormat:
    out: RecordFormat = {}  # type: ignore[typeddict-item]
    if "RecordFormatType" in data:
        import aws_sdk_kinesis_analytics.types.record_format_type

        out["record_format_type"] = (
            aws_sdk_kinesis_analytics.types.record_format_type.deserialize_aws_json_1_1(
                data["RecordFormatType"]
            )
        )
    else:
        raise DeserializationError("RecordFormat.record_format_type required")
    if "MappingParameters" in data:
        import aws_sdk_kinesis_analytics.types.mapping_parameters

        out["mapping_parameters"] = (
            aws_sdk_kinesis_analytics.types.mapping_parameters.deserialize_aws_json_1_1(
                data["MappingParameters"]
            )
        )
    return out
