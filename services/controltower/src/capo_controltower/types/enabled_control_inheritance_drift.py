"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlInheritanceDrift``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.drift_status


class EnabledControlInheritanceDrift(TypedDict, closed=True):
    status: NotRequired["capo_controltower.types.drift_status.DriftStatus"]
    """<p>The status of inheritance drift for the enabled control, indicating whether inheritance configuration matches expectations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlInheritanceDrift) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_controltower.types.drift_status

        out["status"] = capo_controltower.types.drift_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> EnabledControlInheritanceDrift:
    out: EnabledControlInheritanceDrift = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_controltower.types.drift_status

        out["status"] = capo_controltower.types.drift_status.deserialize_json(
            data["status"]
        )
    return out
