"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SilentAudio``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.state


class SilentAudio(TypedDict, closed=True):
    state: NotRequired["capo_mediaconnect.types.state.State"]
    """<p>Indicates whether the <code>SilentAudio</code> metric is enabled or disabled. </p>"""
    threshold_seconds: NotRequired["int"]
    """<p>Specifies the number of consecutive seconds of silence that triggers an event or alert. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SilentAudio) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_mediaconnect.types.state

        out["state"] = capo_mediaconnect.types.state.serialize_json(value["state"])
    if "threshold_seconds" in value:
        out["thresholdSeconds"] = value["threshold_seconds"]
    return out


def deserialize_json(data: dict) -> SilentAudio:
    out: SilentAudio = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_mediaconnect.types.state

        out["state"] = capo_mediaconnect.types.state.deserialize_json(data["state"])
    if "thresholdSeconds" in data:
        out["threshold_seconds"] = data["thresholdSeconds"]
    return out
