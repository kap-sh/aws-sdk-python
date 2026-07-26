"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessingStopSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.max_duration_in_seconds_u_long


class StreamProcessingStopSelector(TypedDict, closed=True):
    max_duration_in_seconds: NotRequired[
        "capo_rekognition.types.max_duration_in_seconds_u_long.MaxDurationInSecondsULong"
    ]
    """<p> Specifies the maximum amount of time in seconds that you want the stream to be processed. The largest amount of time is 2 minutes. The default is 10 seconds. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessingStopSelector) -> dict:
    out: dict = {}
    if "max_duration_in_seconds" in value:
        out["MaxDurationInSeconds"] = value["max_duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessingStopSelector:
    out: StreamProcessingStopSelector = {}  # type: ignore[typeddict-item]
    if "MaxDurationInSeconds" in data:
        out["max_duration_in_seconds"] = data["MaxDurationInSeconds"]
    return out
