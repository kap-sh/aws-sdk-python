"""Generated from Smithy shape ``com.amazonaws.rekognition#PersonDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.person_detail
    import aws_sdk_rekognition.types.timestamp


class PersonDetection(TypedDict, closed=True):
    timestamp: "aws_sdk_rekognition.types.timestamp.Timestamp"
    """<p>The time, in milliseconds from the start of the video, that the person's path was tracked. Note that <code>Timestamp</code> is not guaranteed to be accurate to the individual frame where the person's path first appears.</p>"""
    person: NotRequired["aws_sdk_rekognition.types.person_detail.PersonDetail"]
    """<p>Details about a person whose path was tracked in a video.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonDetection) -> dict:
    out: dict = {}
    out["Timestamp"] = value.get("timestamp", 0)
    if "person" in value:
        import aws_sdk_rekognition.types.person_detail

        out["Person"] = aws_sdk_rekognition.types.person_detail.serialize_aws_json_1_1(
            value["person"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PersonDetection:
    out: PersonDetection = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    else:
        out["timestamp"] = 0
    if "Person" in data:
        import aws_sdk_rekognition.types.person_detail

        out["person"] = (
            aws_sdk_rekognition.types.person_detail.deserialize_aws_json_1_1(
                data["Person"]
            )
        )
    return out
