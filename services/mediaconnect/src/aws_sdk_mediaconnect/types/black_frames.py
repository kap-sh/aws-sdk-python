"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BlackFrames``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.state


class BlackFrames(TypedDict):
    state: NotRequired["aws_sdk_mediaconnect.types.state.State"]
    """<p> Indicates whether the <code>BlackFrames</code> metric is enabled or disabled..</p>"""
    threshold_seconds: NotRequired["int"]
    """<p> Specifies the number of consecutive seconds of black frames that triggers an event or alert.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlackFrames) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_mediaconnect.types.state

        out["state"] = aws_sdk_mediaconnect.types.state.serialize_json(value["state"])
    if "threshold_seconds" in value:
        out["thresholdSeconds"] = value["threshold_seconds"]
    return out


def deserialize_json(data: dict) -> BlackFrames:
    out: BlackFrames = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_mediaconnect.types.state

        out["state"] = aws_sdk_mediaconnect.types.state.deserialize_json(data["state"])
    if "thresholdSeconds" in data:
        out["threshold_seconds"] = data["thresholdSeconds"]
    return out
