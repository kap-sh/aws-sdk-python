"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineInheritanceDrift``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_drift_status


class EnabledBaselineInheritanceDrift(TypedDict, closed=True):
    status: NotRequired[
        "capo_controltower.types.enabled_baseline_drift_status.EnabledBaselineDriftStatus"
    ]
    """<p>The inheritance drift status for enabled baselines.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineInheritanceDrift) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_controltower.types.enabled_baseline_drift_status

        out["status"] = (
            capo_controltower.types.enabled_baseline_drift_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineInheritanceDrift:
    out: EnabledBaselineInheritanceDrift = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_controltower.types.enabled_baseline_drift_status

        out["status"] = (
            capo_controltower.types.enabled_baseline_drift_status.deserialize_json(
                data["status"]
            )
        )
    return out
