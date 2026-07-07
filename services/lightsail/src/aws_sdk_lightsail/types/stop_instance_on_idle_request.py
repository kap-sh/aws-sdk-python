"""Generated from Smithy shape ``com.amazonaws.lightsail#StopInstanceOnIdleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string


class StopInstanceOnIdleRequest(TypedDict, closed=True):
    threshold: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The value to compare with the duration.</p>"""
    duration: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The amount of idle time in minutes after which your virtual computer will automatically stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopInstanceOnIdleRequest) -> dict:
    out: dict = {}
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    if "duration" in value:
        out["duration"] = value["duration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopInstanceOnIdleRequest:
    out: StopInstanceOnIdleRequest = {}  # type: ignore[typeddict-item]
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    if "duration" in data:
        out["duration"] = data["duration"]
    return out
