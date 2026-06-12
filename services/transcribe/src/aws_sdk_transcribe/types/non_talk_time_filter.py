"""Generated from Smithy shape ``com.amazonaws.transcribe#NonTalkTimeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.absolute_time_range
    import aws_sdk_transcribe.types.boolean
    import aws_sdk_transcribe.types.relative_time_range
    import aws_sdk_transcribe.types.timestamp_milliseconds


class NonTalkTimeFilter(TypedDict):
    threshold: NotRequired[
        "aws_sdk_transcribe.types.timestamp_milliseconds.TimestampMilliseconds"
    ]
    """<p>Specify the duration, in milliseconds, of the period of silence that you want to flag. For example, you can flag a silent period that lasts 30,000 milliseconds.</p>"""
    absolute_time_range: NotRequired[
        "aws_sdk_transcribe.types.absolute_time_range.AbsoluteTimeRange"
    ]
    """<p>Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for a period of silence. See for more detail.</p>"""
    relative_time_range: NotRequired[
        "aws_sdk_transcribe.types.relative_time_range.RelativeTimeRange"
    ]
    """<p>Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for a period of silence. See for more detail.</p>"""
    negate: NotRequired["aws_sdk_transcribe.types.boolean.Boolean"]
    """<p>Set to <code>TRUE</code> to flag periods of speech. Set to <code>FALSE</code> to flag periods of silence</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NonTalkTimeFilter) -> dict:
    out: dict = {}
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
    if "absolute_time_range" in value:
        import aws_sdk_transcribe.types.absolute_time_range

        out["AbsoluteTimeRange"] = (
            aws_sdk_transcribe.types.absolute_time_range.serialize_aws_json_1_1(
                value["absolute_time_range"]
            )
        )
    if "relative_time_range" in value:
        import aws_sdk_transcribe.types.relative_time_range

        out["RelativeTimeRange"] = (
            aws_sdk_transcribe.types.relative_time_range.serialize_aws_json_1_1(
                value["relative_time_range"]
            )
        )
    if "negate" in value:
        out["Negate"] = value["negate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NonTalkTimeFilter:
    out: NonTalkTimeFilter = {}  # type: ignore[typeddict-item]
    if "Threshold" in data:
        out["threshold"] = data["Threshold"]
    if "AbsoluteTimeRange" in data:
        import aws_sdk_transcribe.types.absolute_time_range

        out["absolute_time_range"] = (
            aws_sdk_transcribe.types.absolute_time_range.deserialize_aws_json_1_1(
                data["AbsoluteTimeRange"]
            )
        )
    if "RelativeTimeRange" in data:
        import aws_sdk_transcribe.types.relative_time_range

        out["relative_time_range"] = (
            aws_sdk_transcribe.types.relative_time_range.deserialize_aws_json_1_1(
                data["RelativeTimeRange"]
            )
        )
    if "Negate" in data:
        out["negate"] = data["Negate"]
    return out
