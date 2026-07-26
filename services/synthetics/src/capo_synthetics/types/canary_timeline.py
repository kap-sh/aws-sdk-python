"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryTimeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.timestamp


class CanaryTimeline(TypedDict, closed=True):
    created: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The date and time the canary was created.</p>"""
    last_modified: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The date and time the canary was most recently modified.</p>"""
    last_started: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The date and time that the canary's most recent run started.</p>"""
    last_stopped: NotRequired["capo_synthetics.types.timestamp.Timestamp"]
    """<p>The date and time that the canary's most recent run ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryTimeline) -> dict:
    out: dict = {}
    if "created" in value:
        import capo_synthetics.types.timestamp

        out["Created"] = capo_synthetics.types.timestamp.serialize_json(
            value["created"]
        )
    if "last_modified" in value:
        import capo_synthetics.types.timestamp

        out["LastModified"] = capo_synthetics.types.timestamp.serialize_json(
            value["last_modified"]
        )
    if "last_started" in value:
        import capo_synthetics.types.timestamp

        out["LastStarted"] = capo_synthetics.types.timestamp.serialize_json(
            value["last_started"]
        )
    if "last_stopped" in value:
        import capo_synthetics.types.timestamp

        out["LastStopped"] = capo_synthetics.types.timestamp.serialize_json(
            value["last_stopped"]
        )
    return out


def deserialize_json(data: dict) -> CanaryTimeline:
    out: CanaryTimeline = {}  # type: ignore[typeddict-item]
    if "Created" in data:
        import capo_synthetics.types.timestamp

        out["created"] = capo_synthetics.types.timestamp.deserialize_json(
            data["Created"]
        )
    if "LastModified" in data:
        import capo_synthetics.types.timestamp

        out["last_modified"] = capo_synthetics.types.timestamp.deserialize_json(
            data["LastModified"]
        )
    if "LastStarted" in data:
        import capo_synthetics.types.timestamp

        out["last_started"] = capo_synthetics.types.timestamp.deserialize_json(
            data["LastStarted"]
        )
    if "LastStopped" in data:
        import capo_synthetics.types.timestamp

        out["last_stopped"] = capo_synthetics.types.timestamp.deserialize_json(
            data["LastStopped"]
        )
    return out
