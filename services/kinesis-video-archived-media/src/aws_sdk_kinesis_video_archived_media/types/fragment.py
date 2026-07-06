"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#Fragment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.fragment_number_string
    import aws_sdk_kinesis_video_archived_media.types.long
    import aws_sdk_kinesis_video_archived_media.types.timestamp


class Fragment(TypedDict, closed=True):
    fragment_number: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.fragment_number_string.FragmentNumberString"
    ]
    """<p>The unique identifier of the fragment. This value monotonically increases based on the ingestion order.</p>"""
    fragment_size_in_bytes: "aws_sdk_kinesis_video_archived_media.types.long.Long"
    """<p>The total fragment size, including information about the fragment and contained media data.</p>"""
    producer_timestamp: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.timestamp.Timestamp"
    ]
    """<p>The timestamp from the producer corresponding to the fragment.</p>"""
    server_timestamp: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.timestamp.Timestamp"
    ]
    """<p>The timestamp from the Amazon Web Services server corresponding to the fragment.</p>"""
    fragment_length_in_milliseconds: (
        "aws_sdk_kinesis_video_archived_media.types.long.Long"
    )
    """<p>The playback duration or other time value associated with the fragment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Fragment) -> dict:
    out: dict = {}
    if "fragment_number" in value:
        out["FragmentNumber"] = value["fragment_number"]
    out["FragmentSizeInBytes"] = value.get("fragment_size_in_bytes", 0)
    if "producer_timestamp" in value:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["ProducerTimestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.serialize_json(
                value["producer_timestamp"]
            )
        )
    if "server_timestamp" in value:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["ServerTimestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.serialize_json(
                value["server_timestamp"]
            )
        )
    out["FragmentLengthInMilliseconds"] = value.get(
        "fragment_length_in_milliseconds", 0
    )
    return out


def deserialize_json(data: dict) -> Fragment:
    out: Fragment = {}  # type: ignore[typeddict-item]
    if "FragmentNumber" in data:
        out["fragment_number"] = data["FragmentNumber"]
    if "FragmentSizeInBytes" in data:
        out["fragment_size_in_bytes"] = data["FragmentSizeInBytes"]
    else:
        out["fragment_size_in_bytes"] = 0
    if "ProducerTimestamp" in data:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["producer_timestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["ProducerTimestamp"]
            )
        )
    if "ServerTimestamp" in data:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["server_timestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["ServerTimestamp"]
            )
        )
    if "FragmentLengthInMilliseconds" in data:
        out["fragment_length_in_milliseconds"] = data["FragmentLengthInMilliseconds"]
    else:
        out["fragment_length_in_milliseconds"] = 0
    return out
