"""Generated from Smithy shape ``com.amazonaws.kinesisvideomedia#StartSelector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video_media.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_media.types.continuation_token
    import aws_sdk_kinesis_video_media.types.fragment_number_string
    import aws_sdk_kinesis_video_media.types.start_selector_type
    import aws_sdk_kinesis_video_media.types.timestamp


class StartSelector(TypedDict):
    start_selector_type: (
        "aws_sdk_kinesis_video_media.types.start_selector_type.StartSelectorType"
    )
    """<p>Identifies the fragment on the Kinesis video stream where you want to start getting the data from.</p> <ul> <li> <p>NOW - Start with the latest chunk on the stream.</p> </li> <li> <p>EARLIEST - Start with earliest available chunk on the stream.</p> </li> <li> <p>FRAGMENT_NUMBER - Start with the chunk after a specific fragment. You must also specify the <code>AfterFragmentNumber</code> parameter.</p> </li> <li> <p>PRODUCER_TIMESTAMP or SERVER_TIMESTAMP - Start with the chunk containing a fragment with the specified producer or server timestamp. You specify the timestamp by adding <code>StartTimestamp</code>.</p> </li> <li> <p> CONTINUATION_TOKEN - Read using the specified continuation token. </p> </li> </ul> <note> <p>If you choose the NOW, EARLIEST, or CONTINUATION_TOKEN as the <code>startSelectorType</code>, you don't provide any additional information in the <code>startSelector</code>.</p> </note>"""
    after_fragment_number: NotRequired[
        "aws_sdk_kinesis_video_media.types.fragment_number_string.FragmentNumberString"
    ]
    """<p>Specifies the fragment number from where you want the <code>GetMedia</code> API to start returning the fragments. </p>"""
    start_timestamp: NotRequired[
        "aws_sdk_kinesis_video_media.types.timestamp.Timestamp"
    ]
    """<p>A timestamp value. This value is required if you choose the PRODUCER_TIMESTAMP or the SERVER_TIMESTAMP as the <code>startSelectorType</code>. The <code>GetMedia</code> API then starts with the chunk containing the fragment that has the specified timestamp.</p>"""
    continuation_token: NotRequired[
        "aws_sdk_kinesis_video_media.types.continuation_token.ContinuationToken"
    ]
    """<p>Continuation token that Kinesis Video Streams returned in the previous <code>GetMedia</code> response. The <code>GetMedia</code> API then starts with the chunk identified by the continuation token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSelector) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_video_media.types.start_selector_type

    out["StartSelectorType"] = (
        aws_sdk_kinesis_video_media.types.start_selector_type.serialize_json(
            value["start_selector_type"]
        )
    )
    if "after_fragment_number" in value:
        out["AfterFragmentNumber"] = value["after_fragment_number"]
    if "start_timestamp" in value:
        import aws_sdk_kinesis_video_media.types.timestamp

        out["StartTimestamp"] = (
            aws_sdk_kinesis_video_media.types.timestamp.serialize_json(
                value["start_timestamp"]
            )
        )
    if "continuation_token" in value:
        out["ContinuationToken"] = value["continuation_token"]
    return out


def deserialize_json(data: dict) -> StartSelector:
    out: StartSelector = {}  # type: ignore[typeddict-item]
    if "StartSelectorType" in data:
        import aws_sdk_kinesis_video_media.types.start_selector_type

        out["start_selector_type"] = (
            aws_sdk_kinesis_video_media.types.start_selector_type.deserialize_json(
                data["StartSelectorType"]
            )
        )
    else:
        raise DeserializationError("StartSelector.start_selector_type required")
    if "AfterFragmentNumber" in data:
        out["after_fragment_number"] = data["AfterFragmentNumber"]
    if "StartTimestamp" in data:
        import aws_sdk_kinesis_video_media.types.timestamp

        out["start_timestamp"] = (
            aws_sdk_kinesis_video_media.types.timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    if "ContinuationToken" in data:
        out["continuation_token"] = data["ContinuationToken"]
    return out
