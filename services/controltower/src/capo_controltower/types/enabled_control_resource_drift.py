"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlResourceDrift``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.drift_status


class EnabledControlResourceDrift(TypedDict, closed=True):
    status: NotRequired["capo_controltower.types.drift_status.DriftStatus"]
    """<p>The status of resource drift for the enabled control, indicating whether the underlying resources match the expected configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlResourceDrift) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_controltower.types.drift_status

        out["status"] = capo_controltower.types.drift_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> EnabledControlResourceDrift:
    out: EnabledControlResourceDrift = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_controltower.types.drift_status

        out["status"] = capo_controltower.types.drift_status.deserialize_json(
            data["status"]
        )
    return out
