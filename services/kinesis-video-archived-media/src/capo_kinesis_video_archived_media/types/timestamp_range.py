"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#TimestampRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_video_archived_media.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.timestamp


class TimestampRange(TypedDict, closed=True):
    start_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp"
    """<p>The starting timestamp in the range of timestamps for which to return fragments.</p>"""
    end_timestamp: "capo_kinesis_video_archived_media.types.timestamp.Timestamp"
    """<p>The ending timestamp in the range of timestamps for which to return fragments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestampRange) -> dict:
    out: dict = {}
    import capo_kinesis_video_archived_media.types.timestamp

    out["StartTimestamp"] = (
        capo_kinesis_video_archived_media.types.timestamp.serialize_json(
            value["start_timestamp"]
        )
    )
    import capo_kinesis_video_archived_media.types.timestamp

    out["EndTimestamp"] = (
        capo_kinesis_video_archived_media.types.timestamp.serialize_json(
            value["end_timestamp"]
        )
    )
    return out


def deserialize_json(data: dict) -> TimestampRange:
    out: TimestampRange = {}  # type: ignore[typeddict-item]
    if "StartTimestamp" in data:
        import capo_kinesis_video_archived_media.types.timestamp

        out["start_timestamp"] = (
            capo_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    else:
        raise DeserializationError("TimestampRange.start_timestamp required")
    if "EndTimestamp" in data:
        import capo_kinesis_video_archived_media.types.timestamp

        out["end_timestamp"] = (
            capo_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    else:
        raise DeserializationError("TimestampRange.end_timestamp required")
    return out
