"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeTranscriptSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.boolean
    import aws_sdk_transcribe_streaming.types.double
    import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_list
    import aws_sdk_transcribe_streaming.types.string


class MedicalScribeTranscriptSegment(TypedDict, closed=True):
    segment_id: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The identifier of the segment.</p>"""
    begin_audio_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The start time, in milliseconds, of the segment.</p>"""
    end_audio_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The end time, in milliseconds, of the segment.</p>"""
    content: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>Contains transcribed text of the segment.</p>"""
    items: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_list.MedicalScribeTranscriptItemList"
    ]
    """<p>Contains words, phrases, or punctuation marks in your segment.</p>"""
    is_partial: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Indicates if the segment is complete.</p> <p>If <code>IsPartial</code> is <code>true</code>, the segment is not complete. If <code>IsPartial</code> is <code>false</code>, the segment is complete. </p>"""
    channel_id: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>Indicates which audio channel is associated with the <code>MedicalScribeTranscriptSegment</code>. </p> <p>If <code>MedicalScribeChannelDefinition</code> is not provided in the <code>MedicalScribeConfigurationEvent</code>, then this field will not be included. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptSegment) -> dict:
    out: dict = {}
    if "segment_id" in value:
        out["SegmentId"] = value["segment_id"]
    out["BeginAudioTime"] = value.get("begin_audio_time", 0)
    out["EndAudioTime"] = value.get("end_audio_time", 0)
    if "content" in value:
        out["Content"] = value["content"]
    if "items" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_list

        out["Items"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_list.serialize_json(
                value["items"]
            )
        )
    out["IsPartial"] = value.get("is_partial", False)
    if "channel_id" in value:
        out["ChannelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> MedicalScribeTranscriptSegment:
    out: MedicalScribeTranscriptSegment = {}  # type: ignore[typeddict-item]
    if "SegmentId" in data:
        out["segment_id"] = data["SegmentId"]
    if "BeginAudioTime" in data:
        out["begin_audio_time"] = data["BeginAudioTime"]
    else:
        out["begin_audio_time"] = 0
    if "EndAudioTime" in data:
        out["end_audio_time"] = data["EndAudioTime"]
    else:
        out["end_audio_time"] = 0
    if "Content" in data:
        out["content"] = data["Content"]
    if "Items" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_list

        out["items"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_list.deserialize_json(
                data["Items"]
            )
        )
    if "IsPartial" in data:
        out["is_partial"] = data["IsPartial"]
    else:
        out["is_partial"] = False
    if "ChannelId" in data:
        out["channel_id"] = data["ChannelId"]
    return out
