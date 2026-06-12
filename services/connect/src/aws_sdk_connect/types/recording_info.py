"""Generated from Smithy shape ``com.amazonaws.connect#RecordingInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.fragment_number
    import aws_sdk_connect.types.media_stream_type
    import aws_sdk_connect.types.participant_type
    import aws_sdk_connect.types.recording_deletion_reason
    import aws_sdk_connect.types.recording_location
    import aws_sdk_connect.types.recording_status
    import aws_sdk_connect.types.storage_type
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.unprocessed_transcript_location


class RecordingInfo(TypedDict):
    storage_type: NotRequired["aws_sdk_connect.types.storage_type.StorageType"]
    """<p>Where the recording/transcript is stored.</p>"""
    location: NotRequired["aws_sdk_connect.types.recording_location.RecordingLocation"]
    """<p>The location, in Amazon S3, for the recording/transcript.</p>"""
    media_stream_type: NotRequired[
        "aws_sdk_connect.types.media_stream_type.MediaStreamType"
    ]
    """<p>Information about the media stream used during the conversation.</p>"""
    participant_type: NotRequired[
        "aws_sdk_connect.types.participant_type.ParticipantType"
    ]
    """<p>Information about the conversation participant, whether they are an agent or contact. The participant types are as follows:</p> <ul> <li> <p>All</p> </li> <li> <p>Manager</p> </li> <li> <p>Agent</p> </li> <li> <p>Customer</p> </li> <li> <p>Thirdparty</p> </li> <li> <p>Supervisor</p> </li> </ul>"""
    fragment_start_number: NotRequired[
        "aws_sdk_connect.types.fragment_number.FragmentNumber"
    ]
    """<p>The number that identifies the Kinesis Video Streams fragment where the customer audio stream started.</p>"""
    fragment_stop_number: NotRequired[
        "aws_sdk_connect.types.fragment_number.FragmentNumber"
    ]
    """<p>The number that identifies the Kinesis Video Streams fragment where the customer audio stream stopped.</p>"""
    start_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>When the conversation of the last leg of the recording started in UTC time.</p>"""
    stop_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>When the conversation of the last leg of recording stopped in UTC time.</p>"""
    status: NotRequired["aws_sdk_connect.types.recording_status.RecordingStatus"]
    """<p>The status of the recording/transcript.</p>"""
    deletion_reason: NotRequired[
        "aws_sdk_connect.types.recording_deletion_reason.RecordingDeletionReason"
    ]
    """<p>If the recording/transcript was deleted, this is the reason entered for the deletion.</p>"""
    unprocessed_transcript_location: NotRequired[
        "aws_sdk_connect.types.unprocessed_transcript_location.UnprocessedTranscriptLocation"
    ]
    """<p> The location, in Amazon S3, for the unprocessed transcript if any media processing was performed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordingInfo) -> dict:
    out: dict = {}
    if "storage_type" in value:
        import aws_sdk_connect.types.storage_type

        out["StorageType"] = aws_sdk_connect.types.storage_type.serialize_json(
            value["storage_type"]
        )
    if "location" in value:
        out["Location"] = value["location"]
    if "media_stream_type" in value:
        import aws_sdk_connect.types.media_stream_type

        out["MediaStreamType"] = aws_sdk_connect.types.media_stream_type.serialize_json(
            value["media_stream_type"]
        )
    if "participant_type" in value:
        import aws_sdk_connect.types.participant_type

        out["ParticipantType"] = aws_sdk_connect.types.participant_type.serialize_json(
            value["participant_type"]
        )
    if "fragment_start_number" in value:
        out["FragmentStartNumber"] = value["fragment_start_number"]
    if "fragment_stop_number" in value:
        out["FragmentStopNumber"] = value["fragment_stop_number"]
    if "start_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["StartTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["start_timestamp"]
        )
    if "stop_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["StopTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["stop_timestamp"]
        )
    if "status" in value:
        import aws_sdk_connect.types.recording_status

        out["Status"] = aws_sdk_connect.types.recording_status.serialize_json(
            value["status"]
        )
    if "deletion_reason" in value:
        out["DeletionReason"] = value["deletion_reason"]
    if "unprocessed_transcript_location" in value:
        out["UnprocessedTranscriptLocation"] = value["unprocessed_transcript_location"]
    return out


def deserialize_json(data: dict) -> RecordingInfo:
    out: RecordingInfo = {}  # type: ignore[typeddict-item]
    if "StorageType" in data:
        import aws_sdk_connect.types.storage_type

        out["storage_type"] = aws_sdk_connect.types.storage_type.deserialize_json(
            data["StorageType"]
        )
    if "Location" in data:
        out["location"] = data["Location"]
    if "MediaStreamType" in data:
        import aws_sdk_connect.types.media_stream_type

        out["media_stream_type"] = (
            aws_sdk_connect.types.media_stream_type.deserialize_json(
                data["MediaStreamType"]
            )
        )
    if "ParticipantType" in data:
        import aws_sdk_connect.types.participant_type

        out["participant_type"] = (
            aws_sdk_connect.types.participant_type.deserialize_json(
                data["ParticipantType"]
            )
        )
    if "FragmentStartNumber" in data:
        out["fragment_start_number"] = data["FragmentStartNumber"]
    if "FragmentStopNumber" in data:
        out["fragment_stop_number"] = data["FragmentStopNumber"]
    if "StartTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["start_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["StartTimestamp"]
        )
    if "StopTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["stop_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["StopTimestamp"]
        )
    if "Status" in data:
        import aws_sdk_connect.types.recording_status

        out["status"] = aws_sdk_connect.types.recording_status.deserialize_json(
            data["Status"]
        )
    if "DeletionReason" in data:
        out["deletion_reason"] = data["DeletionReason"]
    if "UnprocessedTranscriptLocation" in data:
        out["unprocessed_transcript_location"] = data["UnprocessedTranscriptLocation"]
    return out
