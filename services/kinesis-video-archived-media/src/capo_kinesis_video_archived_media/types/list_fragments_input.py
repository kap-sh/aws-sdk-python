"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ListFragmentsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.fragment_selector
    import capo_kinesis_video_archived_media.types.list_fragments_max_results
    import capo_kinesis_video_archived_media.types.next_token
    import capo_kinesis_video_archived_media.types.resource_arn
    import capo_kinesis_video_archived_media.types.stream_name


class ListFragmentsInput(TypedDict, closed=True):
    stream_name: NotRequired[
        "capo_kinesis_video_archived_media.types.stream_name.StreamName"
    ]
    """<p>The name of the stream from which to retrieve a fragment list. Specify either this parameter or the <code>StreamARN</code> parameter.</p>"""
    stream_arn: NotRequired[
        "capo_kinesis_video_archived_media.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the stream from which to retrieve a fragment list. Specify either this parameter or the <code>StreamName</code> parameter.</p>"""
    max_results: NotRequired[
        "capo_kinesis_video_archived_media.types.list_fragments_max_results.ListFragmentsMaxResults"
    ]
    """<p>The total number of fragments to return. If the total number of fragments available is more than the value specified in <code>max-results</code>, then a <a>ListFragmentsOutput$NextToken</a> is provided in the output that you can use to resume pagination.</p>"""
    next_token: NotRequired[
        "capo_kinesis_video_archived_media.types.next_token.NextToken"
    ]
    """<p>A token to specify where to start paginating. This is the <a>ListFragmentsOutput$NextToken</a> from a previously truncated response.</p>"""
    fragment_selector: NotRequired[
        "capo_kinesis_video_archived_media.types.fragment_selector.FragmentSelector"
    ]
    """<p>Describes the timestamp range and timestamp origin for the range of fragments to return.</p> <note> <p>This is only required when the <code>NextToken</code> isn't passed in the API.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFragmentsInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "fragment_selector" in value:
        import capo_kinesis_video_archived_media.types.fragment_selector

        out["FragmentSelector"] = (
            capo_kinesis_video_archived_media.types.fragment_selector.serialize_json(
                value["fragment_selector"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListFragmentsInput:
    out: ListFragmentsInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FragmentSelector" in data:
        import capo_kinesis_video_archived_media.types.fragment_selector

        out["fragment_selector"] = (
            capo_kinesis_video_archived_media.types.fragment_selector.deserialize_json(
                data["FragmentSelector"]
            )
        )
    return out
