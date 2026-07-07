"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeStreamSummaryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.stream_description_summary


class DescribeStreamSummaryOutput(TypedDict, closed=True):
    stream_description_summary: (
        "aws_sdk_kinesis.types.stream_description_summary.StreamDescriptionSummary"
    )
    """<p>A <a>StreamDescriptionSummary</a> containing information about the stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStreamSummaryOutput) -> dict:
    out: dict = {}
    import aws_sdk_kinesis.types.stream_description_summary

    out["StreamDescriptionSummary"] = (
        aws_sdk_kinesis.types.stream_description_summary.serialize_aws_json_1_1(
            value["stream_description_summary"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStreamSummaryOutput:
    out: DescribeStreamSummaryOutput = {}  # type: ignore[typeddict-item]
    if "StreamDescriptionSummary" in data:
        import aws_sdk_kinesis.types.stream_description_summary

        out["stream_description_summary"] = (
            aws_sdk_kinesis.types.stream_description_summary.deserialize_aws_json_1_1(
                data["StreamDescriptionSummary"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeStreamSummaryOutput.stream_description_summary required"
        )
    return out
