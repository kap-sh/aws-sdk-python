"""Generated from Smithy shape ``com.amazonaws.rekognition#CelebrityRecognition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.celebrity_detail
    import aws_sdk_rekognition.types.timestamp


class CelebrityRecognition(TypedDict, closed=True):
    timestamp: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>The time, in milliseconds from the start of the video, that the celebrity was recognized. Note that <code>Timestamp</code> is not guaranteed to be accurate to the individual frame where the celebrity first appears.</p>"""
    celebrity: NotRequired["aws_sdk_rekognition.types.celebrity_detail.CelebrityDetail"]
    """<p>Information about a recognized celebrity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CelebrityRecognition) -> dict:
    out: dict = {}
    out["Timestamp"] = value.get("timestamp", 0)
    if "celebrity" in value:
        import aws_sdk_rekognition.types.celebrity_detail

        out["Celebrity"] = (
            aws_sdk_rekognition.types.celebrity_detail.serialize_aws_json_1_1(
                value["celebrity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CelebrityRecognition:
    out: CelebrityRecognition = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    else:
        out["timestamp"] = 0
    if "Celebrity" in data:
        import aws_sdk_rekognition.types.celebrity_detail

        out["celebrity"] = (
            aws_sdk_rekognition.types.celebrity_detail.deserialize_aws_json_1_1(
                data["Celebrity"]
            )
        )
    return out
