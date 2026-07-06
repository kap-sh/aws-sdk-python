"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentModerationDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.content_types
    import aws_sdk_rekognition.types.moderation_label
    import aws_sdk_rekognition.types.timestamp
    import aws_sdk_rekognition.types.u_long


class ContentModerationDetection(TypedDict, closed=True):
    timestamp: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>Time, in milliseconds from the beginning of the video, that the content moderation label was detected. Note that <code>Timestamp</code> is not guaranteed to be accurate to the individual frame where the moderated content first appears.</p>"""
    moderation_label: NotRequired[
        "aws_sdk_rekognition.types.moderation_label.ModerationLabel"
    ]
    """<p>The content moderation label detected by in the stored video.</p>"""
    start_timestamp_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The time in milliseconds defining the start of the timeline segment containing a continuously detected moderation label.</p>"""
    end_timestamp_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p> The time in milliseconds defining the end of the timeline segment containing a continuously detected moderation label. </p>"""
    duration_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p> The time duration of a segment in milliseconds, I.e. time elapsed from StartTimestampMillis to EndTimestampMillis. </p>"""
    content_types: NotRequired["aws_sdk_rekognition.types.content_types.ContentTypes"]
    """<p>A list of predicted results for the type of content an image contains. For example, the image content might be from animation, sports, or a video game.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentModerationDetection) -> dict:
    out: dict = {}
    out["Timestamp"] = value.get("timestamp", 0)
    if "moderation_label" in value:
        import aws_sdk_rekognition.types.moderation_label

        out["ModerationLabel"] = (
            aws_sdk_rekognition.types.moderation_label.serialize_aws_json_1_1(
                value["moderation_label"]
            )
        )
    if "start_timestamp_millis" in value:
        out["StartTimestampMillis"] = value["start_timestamp_millis"]
    if "end_timestamp_millis" in value:
        out["EndTimestampMillis"] = value["end_timestamp_millis"]
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    if "content_types" in value:
        import aws_sdk_rekognition.types.content_types

        out["ContentTypes"] = (
            aws_sdk_rekognition.types.content_types.serialize_aws_json_1_1(
                value["content_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContentModerationDetection:
    out: ContentModerationDetection = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    else:
        out["timestamp"] = 0
    if "ModerationLabel" in data:
        import aws_sdk_rekognition.types.moderation_label

        out["moderation_label"] = (
            aws_sdk_rekognition.types.moderation_label.deserialize_aws_json_1_1(
                data["ModerationLabel"]
            )
        )
    if "StartTimestampMillis" in data:
        out["start_timestamp_millis"] = data["StartTimestampMillis"]
    if "EndTimestampMillis" in data:
        out["end_timestamp_millis"] = data["EndTimestampMillis"]
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    if "ContentTypes" in data:
        import aws_sdk_rekognition.types.content_types

        out["content_types"] = (
            aws_sdk_rekognition.types.content_types.deserialize_aws_json_1_1(
                data["ContentTypes"]
            )
        )
    return out
