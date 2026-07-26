"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDriftStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_drift_types


class EnabledBaselineDriftStatusSummary(TypedDict, closed=True):
    types: NotRequired[
        "capo_controltower.types.enabled_baseline_drift_types.EnabledBaselineDriftTypes"
    ]
    """<p>The types of drift that can be detected for an enabled baseline. Amazon Web Services Control Tower detects inheritance drift on enabled baselines that apply at the OU level. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineDriftStatusSummary) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_controltower.types.enabled_baseline_drift_types

        out["types"] = (
            capo_controltower.types.enabled_baseline_drift_types.serialize_json(
                value["types"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineDriftStatusSummary:
    out: EnabledBaselineDriftStatusSummary = {}  # type: ignore[typeddict-item]
    if "types" in data:
        import capo_controltower.types.enabled_baseline_drift_types

        out["types"] = (
            capo_controltower.types.enabled_baseline_drift_types.deserialize_json(
                data["types"]
            )
        )
    return out
