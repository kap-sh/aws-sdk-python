"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.stream_summary

StreamSummaryList: TypeAlias = list[
    "aws_sdk_kinesis.types.stream_summary.StreamSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamSummaryList) -> list:
    import aws_sdk_kinesis.types.stream_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_kinesis.types.stream_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StreamSummaryList:
    import aws_sdk_kinesis.types.stream_summary

    out: StreamSummaryList = []
    for item in data:
        out.append(aws_sdk_kinesis.types.stream_summary.deserialize_aws_json_1_1(item))
    return out
