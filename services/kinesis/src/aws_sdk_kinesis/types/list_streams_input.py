"""Generated from Smithy shape ``com.amazonaws.kinesis#ListStreamsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.list_streams_input_limit
    import aws_sdk_kinesis.types.next_token
    import aws_sdk_kinesis.types.stream_name


class ListStreamsInput(TypedDict, closed=True):
    limit: NotRequired[
        "aws_sdk_kinesis.types.list_streams_input_limit.ListStreamsInputLimit"
    ]
    """<p>The maximum number of streams to list. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.</p>"""
    exclusive_start_stream_name: NotRequired[
        "aws_sdk_kinesis.types.stream_name.StreamName"
    ]
    """<p>The name of the stream to start the list with.</p>"""
    next_token: NotRequired["aws_sdk_kinesis.types.next_token.NextToken"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStreamsInput) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "exclusive_start_stream_name" in value:
        out["ExclusiveStartStreamName"] = value["exclusive_start_stream_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStreamsInput:
    out: ListStreamsInput = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "ExclusiveStartStreamName" in data:
        out["exclusive_start_stream_name"] = data["ExclusiveStartStreamName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
