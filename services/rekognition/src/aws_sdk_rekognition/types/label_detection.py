"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.label
    import aws_sdk_rekognition.types.timestamp
    import aws_sdk_rekognition.types.u_long


class LabelDetection(TypedDict):
    timestamp: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>Time, in milliseconds from the start of the video, that the label was detected. Note that <code>Timestamp</code> is not guaranteed to be accurate to the individual frame where the label first appears.</p>"""
    label: NotRequired["aws_sdk_rekognition.types.label.Label"]
    """<p>Details about the detected label.</p>"""
    start_timestamp_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The time in milliseconds defining the start of the timeline segment containing a continuously detected label.</p>"""
    end_timestamp_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The time in milliseconds defining the end of the timeline segment containing a continuously detected label.</p>"""
    duration_millis: NotRequired["aws_sdk_rekognition.types.u_long.ULong"]
    """<p>The time duration of a segment in milliseconds, I.e. time elapsed from StartTimestampMillis to EndTimestampMillis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelDetection) -> dict:
    out: dict = {}
    out["Timestamp"] = value.get("timestamp", 0)
    if "label" in value:
        import aws_sdk_rekognition.types.label

        out["Label"] = aws_sdk_rekognition.types.label.serialize_aws_json_1_1(
            value["label"]
        )
    if "start_timestamp_millis" in value:
        out["StartTimestampMillis"] = value["start_timestamp_millis"]
    if "end_timestamp_millis" in value:
        out["EndTimestampMillis"] = value["end_timestamp_millis"]
    if "duration_millis" in value:
        out["DurationMillis"] = value["duration_millis"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelDetection:
    out: LabelDetection = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    else:
        out["timestamp"] = 0
    if "Label" in data:
        import aws_sdk_rekognition.types.label

        out["label"] = aws_sdk_rekognition.types.label.deserialize_aws_json_1_1(
            data["Label"]
        )
    if "StartTimestampMillis" in data:
        out["start_timestamp_millis"] = data["StartTimestampMillis"]
    if "EndTimestampMillis" in data:
        out["end_timestamp_millis"] = data["EndTimestampMillis"]
    if "DurationMillis" in data:
        out["duration_millis"] = data["DurationMillis"]
    return out
