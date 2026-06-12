"""Generated from Smithy shape ``com.amazonaws.rekognition#SegmentDetection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.segment_type
    import aws_sdk_rekognition.types.shot_segment
    import aws_sdk_rekognition.types.technical_cue_segment
    import aws_sdk_rekognition.types.timecode
    import aws_sdk_rekognition.types.timestamp
    import aws_sdk_rekognition.types.u_long


class SegmentDetection(TypedDict):
    type: NotRequired["aws_sdk_rekognition.types.segment_type.SegmentType"]
    """<p>The type of the segment. Valid values are <code>TECHNICAL_CUE</code> and <code>SHOT</code>.</p>"""
    start_timestamp_millis: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>The start time of the detected segment in milliseconds from the start of the video. This value is rounded down. For example, if the actual timestamp is 100.6667 milliseconds, Amazon Rekognition Video returns a value of 100 millis.</p>"""
    end_timestamp_millis: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>The end time of the detected segment, in milliseconds, from the start of the video. This value is rounded down.</p>"""
    duration_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The duration of the detected segment in milliseconds. </p>"""
    start_timecode_smpte: NotRequired["aws_sdk_rekognition.types.timecode.Timecode"]
    """<p>The frame-accurate SMPTE timecode, from the start of a video, for the start of a detected segment. <code>StartTimecode</code> is in <i>HH:MM:SS:fr</i> format (and <i>;fr</i> for drop frame-rates). </p>"""
    end_timecode_smpte: NotRequired["aws_sdk_rekognition.types.timecode.Timecode"]
    """<p>The frame-accurate SMPTE timecode, from the start of a video, for the end of a detected segment. <code>EndTimecode</code> is in <i>HH:MM:SS:fr</i> format (and <i>;fr</i> for drop frame-rates).</p>"""
    duration_smpte: NotRequired["aws_sdk_rekognition.types.timecode.Timecode"]
    """<p>The duration of the timecode for the detected segment in SMPTE format.</p>"""
    technical_cue_segment: NotRequired[
        "aws_sdk_rekognition.types.technical_cue_segment.TechnicalCueSegment"
    ]
    """<p>If the segment is a technical cue, contains information about the technical cue.</p>"""
    shot_segment: NotRequired["aws_sdk_rekognition.types.shot_segment.ShotSegment"]
    """<p>If the segment is a shot detection, contains information about the shot detection.</p>"""
    start_frame_number: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p> The frame number of the start of a video segment, using a frame index that starts with 0. </p>"""
    end_frame_number: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p> The frame number at the end of a video segment, using a frame index that starts with 0. </p>"""
    duration_frames: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p> The duration of a video segment, expressed in frames. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SegmentDetection) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_rekognition.types.segment_type

        out["Type"] = aws_sdk_rekognition.types.segment_type.serialize_aws_json_1_1(
            value["type"]
        )
    out["StartTimestampMillis"] = value.get("start_timestamp_millis", 0)
    out["EndTimestampMillis"] = value.get("end_timestamp_millis", 0)
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    if "start_timecode_smpte" in value:
        out["StartTimecodeSMPTE"] = value["start_timecode_smpte"]
    if "end_timecode_smpte" in value:
        out["EndTimecodeSMPTE"] = value["end_timecode_smpte"]
    if "duration_smpte" in value:
        out["DurationSMPTE"] = value["duration_smpte"]
    if "technical_cue_segment" in value:
        import aws_sdk_rekognition.types.technical_cue_segment

        out["TechnicalCueSegment"] = (
            aws_sdk_rekognition.types.technical_cue_segment.serialize_aws_json_1_1(
                value["technical_cue_segment"]
            )
        )
    if "shot_segment" in value:
        import aws_sdk_rekognition.types.shot_segment

        out["ShotSegment"] = (
            aws_sdk_rekognition.types.shot_segment.serialize_aws_json_1_1(
                value["shot_segment"]
            )
        )
    if "start_frame_number" in value:
        out["StartFrameNumber"] = value["start_frame_number"]
    if "end_frame_number" in value:
        out["EndFrameNumber"] = value["end_frame_number"]
    if "duration_frames" in value:
        out["DurationFrames"] = value["duration_frames"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SegmentDetection:
    out: SegmentDetection = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_rekognition.types.segment_type

        out["type"] = aws_sdk_rekognition.types.segment_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "StartTimestampMillis" in data:
        out["start_timestamp_millis"] = data["StartTimestampMillis"]
    else:
        out["start_timestamp_millis"] = 0
    if "EndTimestampMillis" in data:
        out["end_timestamp_millis"] = data["EndTimestampMillis"]
    else:
        out["end_timestamp_millis"] = 0
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    if "StartTimecodeSMPTE" in data:
        out["start_timecode_smpte"] = data["StartTimecodeSMPTE"]
    if "EndTimecodeSMPTE" in data:
        out["end_timecode_smpte"] = data["EndTimecodeSMPTE"]
    if "DurationSMPTE" in data:
        out["duration_smpte"] = data["DurationSMPTE"]
    if "TechnicalCueSegment" in data:
        import aws_sdk_rekognition.types.technical_cue_segment

        out["technical_cue_segment"] = (
            aws_sdk_rekognition.types.technical_cue_segment.deserialize_aws_json_1_1(
                data["TechnicalCueSegment"]
            )
        )
    if "ShotSegment" in data:
        import aws_sdk_rekognition.types.shot_segment

        out["shot_segment"] = (
            aws_sdk_rekognition.types.shot_segment.deserialize_aws_json_1_1(
                data["ShotSegment"]
            )
        )
    if "StartFrameNumber" in data:
        out["start_frame_number"] = data["StartFrameNumber"]
    if "EndFrameNumber" in data:
        out["end_frame_number"] = data["EndFrameNumber"]
    if "DurationFrames" in data:
        out["duration_frames"] = data["DurationFrames"]
    return out
