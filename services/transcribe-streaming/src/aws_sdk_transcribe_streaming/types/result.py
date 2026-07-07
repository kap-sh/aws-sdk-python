"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Result``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.alternative_list
    import aws_sdk_transcribe_streaming.types.boolean
    import aws_sdk_transcribe_streaming.types.double
    import aws_sdk_transcribe_streaming.types.language_code
    import aws_sdk_transcribe_streaming.types.language_identification
    import aws_sdk_transcribe_streaming.types.string


class Result(TypedDict, closed=True):
    result_id: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>Provides a unique identifier for the <code>Result</code>.</p>"""
    start_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The start time of the <code>Result</code> in seconds, with millisecond precision (e.g., 1.056).</p>"""
    end_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The end time of the <code>Result</code> in seconds, with millisecond precision (e.g., 1.056).</p>"""
    is_partial: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Indicates if the segment is complete.</p> <p>If <code>IsPartial</code> is <code>true</code>, the segment is not complete. If <code>IsPartial</code> is <code>false</code>, the segment is complete.</p>"""
    alternatives: NotRequired[
        "aws_sdk_transcribe_streaming.types.alternative_list.AlternativeList"
    ]
    """<p>A list of possible alternative transcriptions for the input audio. Each alternative may contain one or more of <code>Items</code>, <code>Entities</code>, or <code>Transcript</code>.</p>"""
    channel_id: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>Indicates which audio channel is associated with the <code>Result</code>.</p>"""
    language_code: NotRequired[
        "aws_sdk_transcribe_streaming.types.language_code.LanguageCode"
    ]
    """<p>The language code that represents the language spoken in your audio stream.</p>"""
    language_identification: NotRequired[
        "aws_sdk_transcribe_streaming.types.language_identification.LanguageIdentification"
    ]
    """<p>The language code of the dominant language identified in your stream.</p> <p>If you enabled channel identification and each channel of your audio contains a different language, you may have more than one result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Result) -> dict:
    out: dict = {}
    if "result_id" in value:
        out["ResultId"] = value["result_id"]
    out["StartTime"] = value.get("start_time", 0)
    out["EndTime"] = value.get("end_time", 0)
    out["IsPartial"] = value.get("is_partial", False)
    if "alternatives" in value:
        import aws_sdk_transcribe_streaming.types.alternative_list

        out["Alternatives"] = (
            aws_sdk_transcribe_streaming.types.alternative_list.serialize_json(
                value["alternatives"]
            )
        )
    if "channel_id" in value:
        out["ChannelId"] = value["channel_id"]
    if "language_code" in value:
        import aws_sdk_transcribe_streaming.types.language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe_streaming.types.language_code.serialize_json(
                value["language_code"]
            )
        )
    if "language_identification" in value:
        import aws_sdk_transcribe_streaming.types.language_identification

        out["LanguageIdentification"] = (
            aws_sdk_transcribe_streaming.types.language_identification.serialize_json(
                value["language_identification"]
            )
        )
    return out


def deserialize_json(data: dict) -> Result:
    out: Result = {}  # type: ignore[typeddict-item]
    if "ResultId" in data:
        out["result_id"] = data["ResultId"]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    else:
        out["start_time"] = 0
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    else:
        out["end_time"] = 0
    if "IsPartial" in data:
        out["is_partial"] = data["IsPartial"]
    else:
        out["is_partial"] = False
    if "Alternatives" in data:
        import aws_sdk_transcribe_streaming.types.alternative_list

        out["alternatives"] = (
            aws_sdk_transcribe_streaming.types.alternative_list.deserialize_json(
                data["Alternatives"]
            )
        )
    if "ChannelId" in data:
        out["channel_id"] = data["ChannelId"]
    if "LanguageCode" in data:
        import aws_sdk_transcribe_streaming.types.language_code

        out["language_code"] = (
            aws_sdk_transcribe_streaming.types.language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if "LanguageIdentification" in data:
        import aws_sdk_transcribe_streaming.types.language_identification

        out["language_identification"] = (
            aws_sdk_transcribe_streaming.types.language_identification.deserialize_json(
                data["LanguageIdentification"]
            )
        )
    return out
