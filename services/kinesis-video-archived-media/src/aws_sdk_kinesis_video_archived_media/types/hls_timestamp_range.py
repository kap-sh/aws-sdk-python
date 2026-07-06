"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSTimestampRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.timestamp


class HLSTimestampRange(TypedDict, closed=True):
    start_timestamp: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.timestamp.Timestamp"
    ]
    """<p>The start of the timestamp range for the requested media.</p> <p>If the <code>HLSTimestampRange</code> value is specified, the <code>StartTimestamp</code> value is required. </p> <p>Only fragments that start exactly at or after <code>StartTimestamp</code> are included in the session. Fragments that start before <code>StartTimestamp</code> and continue past it aren't included in the session. If <code>FragmentSelectorType</code> is <code>SERVER_TIMESTAMP</code>, the <code>StartTimestamp</code> must be later than the stream head. </p>"""
    end_timestamp: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.timestamp.Timestamp"
    ]
    """<p>The end of the timestamp range for the requested media. This value must be within 24 hours of the specified <code>StartTimestamp</code>, and it must be later than the <code>StartTimestamp</code> value.</p> <p>If <code>FragmentSelectorType</code> for the request is <code>SERVER_TIMESTAMP</code>, this value must be in the past.</p> <p>The <code>EndTimestamp</code> value is required for <code>ON_DEMAND</code> mode, but optional for <code>LIVE_REPLAY</code> mode. If the <code>EndTimestamp</code> is not set for <code>LIVE_REPLAY</code> mode then the session will continue to include newly ingested fragments until the session expires.</p> <note> <p>This value is inclusive. The <code>EndTimestamp</code> is compared to the (starting) timestamp of the fragment. Fragments that start before the <code>EndTimestamp</code> value and continue past it are included in the session.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: HLSTimestampRange) -> dict:
    out: dict = {}
    if "start_timestamp" in value:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["StartTimestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.serialize_json(
                value["start_timestamp"]
            )
        )
    if "end_timestamp" in value:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["EndTimestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.serialize_json(
                value["end_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> HLSTimestampRange:
    out: HLSTimestampRange = {}  # type: ignore[typeddict-item]
    if "StartTimestamp" in data:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["start_timestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    if "EndTimestamp" in data:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["end_timestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    return out
