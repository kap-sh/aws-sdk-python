"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListStreamsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.list_streams_input_limit
    import capo_kinesis_video.types.next_token
    import capo_kinesis_video.types.stream_name_condition


class ListStreamsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_kinesis_video.types.list_streams_input_limit.ListStreamsInputLimit"
    ]
    """<p>The maximum number of streams to return in the response. The default is 10,000.</p>"""
    next_token: NotRequired["capo_kinesis_video.types.next_token.NextToken"]
    """<p>If you specify this parameter, when the result of a <code>ListStreams</code> operation is truncated, the call returns the <code>NextToken</code> in the response. To get another batch of streams, provide this token in your next request.</p>"""
    stream_name_condition: NotRequired[
        "capo_kinesis_video.types.stream_name_condition.StreamNameCondition"
    ]
    """<p>Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only the prefix of a stream name as a condition. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "stream_name_condition" in value:
        import capo_kinesis_video.types.stream_name_condition

        out["StreamNameCondition"] = (
            capo_kinesis_video.types.stream_name_condition.serialize_json(
                value["stream_name_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListStreamsInput:
    out: ListStreamsInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "StreamNameCondition" in data:
        import capo_kinesis_video.types.stream_name_condition

        out["stream_name_condition"] = (
            capo_kinesis_video.types.stream_name_condition.deserialize_json(
                data["StreamNameCondition"]
            )
        )
    return out
