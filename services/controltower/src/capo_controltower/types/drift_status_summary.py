"""Generated from Smithy shape ``com.amazonaws.controltower#DriftStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.drift_status
    import capo_controltower.types.enabled_control_drift_types


class DriftStatusSummary(TypedDict, closed=True):
    drift_status: NotRequired["capo_controltower.types.drift_status.DriftStatus"]
    """<p> The drift status of the enabled control.</p> <p>Valid values:</p> <ul> <li> <p> <code>DRIFTED</code>: The <code>enabledControl</code> deployed in this configuration doesn’t match the configuration that Amazon Web Services Control Tower expected. </p> </li> <li> <p> <code>IN_SYNC</code>: The <code>enabledControl</code> deployed in this configuration matches the configuration that Amazon Web Services Control Tower expected.</p> </li> <li> <p> <code>NOT_CHECKING</code>: Amazon Web Services Control Tower does not check drift for this enabled control. Drift is not supported for the control type.</p> </li> <li> <p> <code>UNKNOWN</code>: Amazon Web Services Control Tower is not able to check the drift status for the enabled control. </p> </li> </ul>"""
    types: NotRequired[
        "capo_controltower.types.enabled_control_drift_types.EnabledControlDriftTypes"
    ]
    """<p>An object that categorizes the different types of drift detected for the enabled control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DriftStatusSummary) -> dict:
    out: dict = {}
    if "drift_status" in value:
        import capo_controltower.types.drift_status

        out["driftStatus"] = capo_controltower.types.drift_status.serialize_json(
            value["drift_status"]
        )
    if "types" in value:
        import capo_controltower.types.enabled_control_drift_types

        out["types"] = (
            capo_controltower.types.enabled_control_drift_types.serialize_json(
                value["types"]
            )
        )
    return out


def deserialize_json(data: dict) -> DriftStatusSummary:
    out: DriftStatusSummary = {}  # type: ignore[typeddict-item]
    if "driftStatus" in data:
        import capo_controltower.types.drift_status

        out["drift_status"] = capo_controltower.types.drift_status.deserialize_json(
            data["driftStatus"]
        )
    if "types" in data:
        import capo_controltower.types.enabled_control_drift_types

        out["types"] = (
            capo_controltower.types.enabled_control_drift_types.deserialize_json(
                data["types"]
            )
        )
    return out
