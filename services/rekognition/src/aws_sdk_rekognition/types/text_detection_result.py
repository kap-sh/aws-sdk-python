"""Generated from Smithy shape ``com.amazonaws.rekognition#TextDetectionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.text_detection
    import aws_sdk_rekognition.types.timestamp


class TextDetectionResult(TypedDict):
    timestamp: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>The time, in milliseconds from the start of the video, that the text was detected. Note that <code>Timestamp</code> is not guaranteed to be accurate to the individual frame where the text first appears.</p>"""
    text_detection: NotRequired[
        "aws_sdk_rekognition.types.text_detection.TextDetection"
    ]
    """<p>Details about text detected in a video.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextDetectionResult) -> dict:
    out: dict = {}
    out["Timestamp"] = value.get("timestamp", 0)
    if "text_detection" in value:
        import aws_sdk_rekognition.types.text_detection

        out["TextDetection"] = (
            aws_sdk_rekognition.types.text_detection.serialize_aws_json_1_1(
                value["text_detection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextDetectionResult:
    out: TextDetectionResult = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    else:
        out["timestamp"] = 0
    if "TextDetection" in data:
        import aws_sdk_rekognition.types.text_detection

        out["text_detection"] = (
            aws_sdk_rekognition.types.text_detection.deserialize_aws_json_1_1(
                data["TextDetection"]
            )
        )
    return out
