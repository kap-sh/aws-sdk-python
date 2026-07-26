"""Generated from Smithy shape ``com.amazonaws.kinesis#ListStreamsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.next_token
    import capo_kinesis.types.stream_name_list
    import capo_kinesis.types.stream_summary_list


class ListStreamsOutput(TypedDict, closed=True):
    stream_names: "capo_kinesis.types.stream_name_list.StreamNameList"
    """<p>The names of the streams that are associated with the Amazon Web Services account making the <code>ListStreams</code> request.</p>"""
    has_more_streams: "capo_kinesis.types.boolean_object.BooleanObject"
    """<p>If set to <code>true</code>, there are more streams available to list.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p></p>"""
    stream_summaries: NotRequired[
        "capo_kinesis.types.stream_summary_list.StreamSummaryList"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStreamsOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.stream_name_list

    out["StreamNames"] = capo_kinesis.types.stream_name_list.serialize_aws_json_1_1(
        value["stream_names"]
    )
    out["HasMoreStreams"] = value["has_more_streams"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "stream_summaries" in value:
        import capo_kinesis.types.stream_summary_list

        out["StreamSummaries"] = (
            capo_kinesis.types.stream_summary_list.serialize_aws_json_1_1(
                value["stream_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStreamsOutput:
    out: ListStreamsOutput = {}  # type: ignore[typeddict-item]
    if "StreamNames" in data:
        import capo_kinesis.types.stream_name_list

        out["stream_names"] = (
            capo_kinesis.types.stream_name_list.deserialize_aws_json_1_1(
                data["StreamNames"]
            )
        )
    else:
        raise DeserializationError("ListStreamsOutput.stream_names required")
    if "HasMoreStreams" in data:
        out["has_more_streams"] = data["HasMoreStreams"]
    else:
        raise DeserializationError("ListStreamsOutput.has_more_streams required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "StreamSummaries" in data:
        import capo_kinesis.types.stream_summary_list

        out["stream_summaries"] = (
            capo_kinesis.types.stream_summary_list.deserialize_aws_json_1_1(
                data["StreamSummaries"]
            )
        )
    return out
