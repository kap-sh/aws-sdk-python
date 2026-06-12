"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DestinationSchema``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.record_format_type


class DestinationSchema(TypedDict):
    record_format_type: (
        "aws_sdk_kinesis_analytics.types.record_format_type.RecordFormatType"
    )
    """<p>Specifies the format of the records on the output stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationSchema) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics.types.record_format_type

    out["RecordFormatType"] = (
        aws_sdk_kinesis_analytics.types.record_format_type.serialize_aws_json_1_1(
            value["record_format_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationSchema:
    out: DestinationSchema = {}  # type: ignore[typeddict-item]
    if "RecordFormatType" in data:
        import aws_sdk_kinesis_analytics.types.record_format_type

        out["record_format_type"] = (
            aws_sdk_kinesis_analytics.types.record_format_type.deserialize_aws_json_1_1(
                data["RecordFormatType"]
            )
        )
    else:
        raise DeserializationError("DestinationSchema.record_format_type required")
    return out
