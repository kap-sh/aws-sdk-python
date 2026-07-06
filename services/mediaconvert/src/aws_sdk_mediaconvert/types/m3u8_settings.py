"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M3u8Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max500
    import aws_sdk_mediaconvert.types.__integer_min0_max1000
    import aws_sdk_mediaconvert.types.__integer_min0_max3600
    import aws_sdk_mediaconvert.types.__integer_min0_max65535
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min32_max8182
    import aws_sdk_mediaconvert.types.__integer_min_negative10000_max10000
    import aws_sdk_mediaconvert.types.__list_of__integer_min32_max8182
    import aws_sdk_mediaconvert.types.m3u8_audio_duration
    import aws_sdk_mediaconvert.types.m3u8_data_pts_control
    import aws_sdk_mediaconvert.types.m3u8_nielsen_id3
    import aws_sdk_mediaconvert.types.m3u8_pcr_control
    import aws_sdk_mediaconvert.types.m3u8_scte35_source
    import aws_sdk_mediaconvert.types.timed_metadata
    import aws_sdk_mediaconvert.types.ts_pts_offset


class M3u8Settings(TypedDict, closed=True):
    audio_duration: NotRequired[
        "aws_sdk_mediaconvert.types.m3u8_audio_duration.M3u8AudioDuration"
    ]
    """Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec."""
    audio_frames_per_pes: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """The number of audio frames to insert for each PES packet."""
    audio_pids: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__integer_min32_max8182.__listOf__integerMin32Max8182"
    ]
    """Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation."""
    audio_pts_offset_delta: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative10000_max10000.__integerMinNegative10000Max10000"
    ]
    """Manually specify the difference in PTS offset that will be applied to the audio track, in seconds or milliseconds, when you set PTS offset to Seconds or Milliseconds. Enter an integer from -10000 to 10000. Leave blank to keep the default value 0."""
    data_pts_control: NotRequired[
        "aws_sdk_mediaconvert.types.m3u8_data_pts_control.M3u8DataPtsControl"
    ]
    """If you select ALIGN_TO_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value AUTO to allow all PTS values."""
    max_pcr_interval: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max500.__integerMin0Max500"
    ]
    """Specify the maximum time, in milliseconds, between Program Clock References (PCRs) inserted into the transport stream."""
    nielsen_id3: NotRequired[
        "aws_sdk_mediaconvert.types.m3u8_nielsen_id3.M3u8NielsenId3"
    ]
    """If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
    pat_interval: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max1000.__integerMin0Max1000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream."""
    pcr_control: NotRequired[
        "aws_sdk_mediaconvert.types.m3u8_pcr_control.M3u8PcrControl"
    ]
    """When set to PCR_EVERY_PES_PACKET a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream."""
    pcr_pid: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID."""
    pmt_interval: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max1000.__integerMin0Max1000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream."""
    pmt_pid: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream."""
    private_metadata_pid: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Packet Identifier (PID) of the private metadata stream in the transport stream."""
    program_number: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """The value of the program number field in the Program Map Table."""
    pts_offset: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max3600.__integerMin0Max3600"
    ]
    """Manually specify the initial PTS offset, in seconds, when you set PTS offset to Seconds. Enter an integer from 0 to 3600. Leave blank to keep the default value 2."""
    pts_offset_mode: NotRequired["aws_sdk_mediaconvert.types.ts_pts_offset.TsPtsOffset"]
    """Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset."""
    scte35_pid: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Packet Identifier (PID) of the SCTE-35 stream in the transport stream."""
    scte35_source: NotRequired[
        "aws_sdk_mediaconvert.types.m3u8_scte35_source.M3u8Scte35Source"
    ]
    """For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. For SCTE-35 markers from an ESAM XML document-- Choose None if you don't want manifest conditioning. Choose Passthrough and choose Ad markers if you do want manifest conditioning. In both cases, also provide the ESAM XML as a string in the setting Signal processing notification XML."""
    timed_metadata: NotRequired[
        "aws_sdk_mediaconvert.types.timed_metadata.TimedMetadata"
    ]
    """Set ID3 metadata to Passthrough to include ID3 metadata in this output. This includes ID3 metadata from the following features: ID3 timestamp period, and Custom ID3 metadata inserter. To exclude this ID3 metadata in this output: set ID3 metadata to None or leave blank."""
    timed_metadata_pid: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Packet Identifier (PID) of the ID3 metadata stream in the transport stream."""
    transport_stream_id: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """The value of the transport stream ID field in the Program Map Table."""
    video_pid: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Packet Identifier (PID) of the elementary video stream in the transport stream."""


# --- restJson1 ser/de ---
def serialize_json(value: M3u8Settings) -> dict:
    out: dict = {}
    if "audio_duration" in value:
        import aws_sdk_mediaconvert.types.m3u8_audio_duration

        out["audioDuration"] = (
            aws_sdk_mediaconvert.types.m3u8_audio_duration.serialize_json(
                value["audio_duration"]
            )
        )
    if "audio_frames_per_pes" in value:
        out["audioFramesPerPes"] = value["audio_frames_per_pes"]
    if "audio_pids" in value:
        import aws_sdk_mediaconvert.types.__list_of__integer_min32_max8182

        out["audioPids"] = (
            aws_sdk_mediaconvert.types.__list_of__integer_min32_max8182.serialize_json(
                value["audio_pids"]
            )
        )
    if "audio_pts_offset_delta" in value:
        out["audioPtsOffsetDelta"] = value["audio_pts_offset_delta"]
    if "data_pts_control" in value:
        import aws_sdk_mediaconvert.types.m3u8_data_pts_control

        out["dataPTSControl"] = (
            aws_sdk_mediaconvert.types.m3u8_data_pts_control.serialize_json(
                value["data_pts_control"]
            )
        )
    if "max_pcr_interval" in value:
        out["maxPcrInterval"] = value["max_pcr_interval"]
    if "nielsen_id3" in value:
        import aws_sdk_mediaconvert.types.m3u8_nielsen_id3

        out["nielsenId3"] = aws_sdk_mediaconvert.types.m3u8_nielsen_id3.serialize_json(
            value["nielsen_id3"]
        )
    if "pat_interval" in value:
        out["patInterval"] = value["pat_interval"]
    if "pcr_control" in value:
        import aws_sdk_mediaconvert.types.m3u8_pcr_control

        out["pcrControl"] = aws_sdk_mediaconvert.types.m3u8_pcr_control.serialize_json(
            value["pcr_control"]
        )
    if "pcr_pid" in value:
        out["pcrPid"] = value["pcr_pid"]
    if "pmt_interval" in value:
        out["pmtInterval"] = value["pmt_interval"]
    if "pmt_pid" in value:
        out["pmtPid"] = value["pmt_pid"]
    if "private_metadata_pid" in value:
        out["privateMetadataPid"] = value["private_metadata_pid"]
    if "program_number" in value:
        out["programNumber"] = value["program_number"]
    if "pts_offset" in value:
        out["ptsOffset"] = value["pts_offset"]
    if "pts_offset_mode" in value:
        import aws_sdk_mediaconvert.types.ts_pts_offset

        out["ptsOffsetMode"] = aws_sdk_mediaconvert.types.ts_pts_offset.serialize_json(
            value["pts_offset_mode"]
        )
    if "scte35_pid" in value:
        out["scte35Pid"] = value["scte35_pid"]
    if "scte35_source" in value:
        import aws_sdk_mediaconvert.types.m3u8_scte35_source

        out["scte35Source"] = (
            aws_sdk_mediaconvert.types.m3u8_scte35_source.serialize_json(
                value["scte35_source"]
            )
        )
    if "timed_metadata" in value:
        import aws_sdk_mediaconvert.types.timed_metadata

        out["timedMetadata"] = aws_sdk_mediaconvert.types.timed_metadata.serialize_json(
            value["timed_metadata"]
        )
    if "timed_metadata_pid" in value:
        out["timedMetadataPid"] = value["timed_metadata_pid"]
    if "transport_stream_id" in value:
        out["transportStreamId"] = value["transport_stream_id"]
    if "video_pid" in value:
        out["videoPid"] = value["video_pid"]
    return out


def deserialize_json(data: dict) -> M3u8Settings:
    out: M3u8Settings = {}  # type: ignore[typeddict-item]
    if "audioDuration" in data:
        import aws_sdk_mediaconvert.types.m3u8_audio_duration

        out["audio_duration"] = (
            aws_sdk_mediaconvert.types.m3u8_audio_duration.deserialize_json(
                data["audioDuration"]
            )
        )
    if "audioFramesPerPes" in data:
        out["audio_frames_per_pes"] = data["audioFramesPerPes"]
    if "audioPids" in data:
        import aws_sdk_mediaconvert.types.__list_of__integer_min32_max8182

        out["audio_pids"] = (
            aws_sdk_mediaconvert.types.__list_of__integer_min32_max8182.deserialize_json(
                data["audioPids"]
            )
        )
    if "audioPtsOffsetDelta" in data:
        out["audio_pts_offset_delta"] = data["audioPtsOffsetDelta"]
    if "dataPTSControl" in data:
        import aws_sdk_mediaconvert.types.m3u8_data_pts_control

        out["data_pts_control"] = (
            aws_sdk_mediaconvert.types.m3u8_data_pts_control.deserialize_json(
                data["dataPTSControl"]
            )
        )
    if "maxPcrInterval" in data:
        out["max_pcr_interval"] = data["maxPcrInterval"]
    if "nielsenId3" in data:
        import aws_sdk_mediaconvert.types.m3u8_nielsen_id3

        out["nielsen_id3"] = (
            aws_sdk_mediaconvert.types.m3u8_nielsen_id3.deserialize_json(
                data["nielsenId3"]
            )
        )
    if "patInterval" in data:
        out["pat_interval"] = data["patInterval"]
    if "pcrControl" in data:
        import aws_sdk_mediaconvert.types.m3u8_pcr_control

        out["pcr_control"] = (
            aws_sdk_mediaconvert.types.m3u8_pcr_control.deserialize_json(
                data["pcrControl"]
            )
        )
    if "pcrPid" in data:
        out["pcr_pid"] = data["pcrPid"]
    if "pmtInterval" in data:
        out["pmt_interval"] = data["pmtInterval"]
    if "pmtPid" in data:
        out["pmt_pid"] = data["pmtPid"]
    if "privateMetadataPid" in data:
        out["private_metadata_pid"] = data["privateMetadataPid"]
    if "programNumber" in data:
        out["program_number"] = data["programNumber"]
    if "ptsOffset" in data:
        out["pts_offset"] = data["ptsOffset"]
    if "ptsOffsetMode" in data:
        import aws_sdk_mediaconvert.types.ts_pts_offset

        out["pts_offset_mode"] = (
            aws_sdk_mediaconvert.types.ts_pts_offset.deserialize_json(
                data["ptsOffsetMode"]
            )
        )
    if "scte35Pid" in data:
        out["scte35_pid"] = data["scte35Pid"]
    if "scte35Source" in data:
        import aws_sdk_mediaconvert.types.m3u8_scte35_source

        out["scte35_source"] = (
            aws_sdk_mediaconvert.types.m3u8_scte35_source.deserialize_json(
                data["scte35Source"]
            )
        )
    if "timedMetadata" in data:
        import aws_sdk_mediaconvert.types.timed_metadata

        out["timed_metadata"] = (
            aws_sdk_mediaconvert.types.timed_metadata.deserialize_json(
                data["timedMetadata"]
            )
        )
    if "timedMetadataPid" in data:
        out["timed_metadata_pid"] = data["timedMetadataPid"]
    if "transportStreamId" in data:
        out["transport_stream_id"] = data["transportStreamId"]
    if "videoPid" in data:
        out["video_pid"] = data["videoPid"]
    return out
