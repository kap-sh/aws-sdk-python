"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ListFragmentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.fragment_list
    import aws_sdk_kinesis_video_archived_media.types.next_token


class ListFragmentsOutput(TypedDict, closed=True):
    fragments: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.fragment_list.FragmentList"
    ]
    """<p>A list of archived <a>Fragment</a> objects from the stream that meet the selector criteria. Results are in no specific order, even across pages.</p>"""
    next_token: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.next_token.NextToken"
    ]
    """<p>If the returned list is truncated, the operation returns this token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFragmentsOutput) -> dict:
    out: dict = {}
    if "fragments" in value:
        import aws_sdk_kinesis_video_archived_media.types.fragment_list

        out["Fragments"] = (
            aws_sdk_kinesis_video_archived_media.types.fragment_list.serialize_json(
                value["fragments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFragmentsOutput:
    out: ListFragmentsOutput = {}  # type: ignore[typeddict-item]
    if "Fragments" in data:
        import aws_sdk_kinesis_video_archived_media.types.fragment_list

        out["fragments"] = (
            aws_sdk_kinesis_video_archived_media.types.fragment_list.deserialize_json(
                data["Fragments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
