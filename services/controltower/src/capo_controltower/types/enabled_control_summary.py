"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.control_identifier
    import capo_controltower.types.drift_status_summary
    import capo_controltower.types.enablement_status_summary
    import capo_controltower.types.parent_identifier
    import capo_controltower.types.target_identifier


class EnabledControlSummary(TypedDict, closed=True):
    arn: NotRequired["capo_controltower.types.arn.Arn"]
    """<p>The ARN of the enabled control.</p>"""
    control_identifier: NotRequired[
        "capo_controltower.types.control_identifier.ControlIdentifier"
    ]
    """<p>The <code>controlIdentifier</code> of the enabled control.</p>"""
    target_identifier: NotRequired[
        "capo_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The ARN of the organizational unit.</p>"""
    status_summary: NotRequired[
        "capo_controltower.types.enablement_status_summary.EnablementStatusSummary"
    ]
    """<p>A short description of the status of the enabled control.</p>"""
    drift_status_summary: NotRequired[
        "capo_controltower.types.drift_status_summary.DriftStatusSummary"
    ]
    """<p>The drift status of the enabled control.</p>"""
    parent_identifier: NotRequired[
        "capo_controltower.types.parent_identifier.ParentIdentifier"
    ]
    """<p>The ARN of the parent enabled control from which this control inherits its configuration, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "control_identifier" in value:
        out["controlIdentifier"] = value["control_identifier"]
    if "target_identifier" in value:
        out["targetIdentifier"] = value["target_identifier"]
    if "status_summary" in value:
        import capo_controltower.types.enablement_status_summary

        out["statusSummary"] = (
            capo_controltower.types.enablement_status_summary.serialize_json(
                value["status_summary"]
            )
        )
    if "drift_status_summary" in value:
        import capo_controltower.types.drift_status_summary

        out["driftStatusSummary"] = (
            capo_controltower.types.drift_status_summary.serialize_json(
                value["drift_status_summary"]
            )
        )
    if "parent_identifier" in value:
        out["parentIdentifier"] = value["parent_identifier"]
    return out


def deserialize_json(data: dict) -> EnabledControlSummary:
    out: EnabledControlSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "controlIdentifier" in data:
        out["control_identifier"] = data["controlIdentifier"]
    if "targetIdentifier" in data:
        out["target_identifier"] = data["targetIdentifier"]
    if "statusSummary" in data:
        import capo_controltower.types.enablement_status_summary

        out["status_summary"] = (
            capo_controltower.types.enablement_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    if "driftStatusSummary" in data:
        import capo_controltower.types.drift_status_summary

        out["drift_status_summary"] = (
            capo_controltower.types.drift_status_summary.deserialize_json(
                data["driftStatusSummary"]
            )
        )
    if "parentIdentifier" in data:
        out["parent_identifier"] = data["parentIdentifier"]
    return out
