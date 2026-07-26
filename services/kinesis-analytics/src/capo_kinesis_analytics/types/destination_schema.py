"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DestinationSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.record_format_type


class DestinationSchema(TypedDict, closed=True):
    record_format_type: (
        "capo_kinesis_analytics.types.record_format_type.RecordFormatType"
    )
    """<p>Specifies the format of the records on the output stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationSchema) -> dict:
    out: dict = {}
    import capo_kinesis_analytics.types.record_format_type

    out["RecordFormatType"] = (
        capo_kinesis_analytics.types.record_format_type.serialize_aws_json_1_1(
            value["record_format_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationSchema:
    out: DestinationSchema = {}  # type: ignore[typeddict-item]
    if "RecordFormatType" in data:
        import capo_kinesis_analytics.types.record_format_type

        out["record_format_type"] = (
            capo_kinesis_analytics.types.record_format_type.deserialize_aws_json_1_1(
                data["RecordFormatType"]
            )
        )
    else:
        raise DeserializationError("DestinationSchema.record_format_type required")
    return out
