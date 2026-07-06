"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_baseline_baseline_identifiers
    import aws_sdk_controltower.types.enabled_baseline_drift_statuses
    import aws_sdk_controltower.types.enabled_baseline_enablement_statuses
    import aws_sdk_controltower.types.enabled_baseline_parent_identifiers
    import aws_sdk_controltower.types.enabled_baseline_target_identifiers


class EnabledBaselineFilter(TypedDict, closed=True):
    target_identifiers: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_target_identifiers.EnabledBaselineTargetIdentifiers"
    ]
    """<p>Identifiers for the targets of the <code>Baseline</code> filter operation.</p>"""
    baseline_identifiers: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_baseline_identifiers.EnabledBaselineBaselineIdentifiers"
    ]
    """<p>Identifiers for the <code>Baseline</code> objects returned as part of the filter operation.</p>"""
    parent_identifiers: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_parent_identifiers.EnabledBaselineParentIdentifiers"
    ]
    """<p>An optional filter that sets up a list of <code>parentIdentifiers</code> to filter the results of the <code>ListEnabledBaseline</code> output.</p>"""
    statuses: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_enablement_statuses.EnabledBaselineEnablementStatuses"
    ]
    """<p>A list of <code>EnablementStatus</code> items.</p>"""
    inheritance_drift_statuses: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_drift_statuses.EnabledBaselineDriftStatuses"
    ]
    """<p>A list of <code>EnabledBaselineDriftStatus</code> items for enabled baselines.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineFilter) -> dict:
    out: dict = {}
    if "target_identifiers" in value:
        import aws_sdk_controltower.types.enabled_baseline_target_identifiers

        out["targetIdentifiers"] = (
            aws_sdk_controltower.types.enabled_baseline_target_identifiers.serialize_json(
                value["target_identifiers"]
            )
        )
    if "baseline_identifiers" in value:
        import aws_sdk_controltower.types.enabled_baseline_baseline_identifiers

        out["baselineIdentifiers"] = (
            aws_sdk_controltower.types.enabled_baseline_baseline_identifiers.serialize_json(
                value["baseline_identifiers"]
            )
        )
    if "parent_identifiers" in value:
        import aws_sdk_controltower.types.enabled_baseline_parent_identifiers

        out["parentIdentifiers"] = (
            aws_sdk_controltower.types.enabled_baseline_parent_identifiers.serialize_json(
                value["parent_identifiers"]
            )
        )
    if "statuses" in value:
        import aws_sdk_controltower.types.enabled_baseline_enablement_statuses

        out["statuses"] = (
            aws_sdk_controltower.types.enabled_baseline_enablement_statuses.serialize_json(
                value["statuses"]
            )
        )
    if "inheritance_drift_statuses" in value:
        import aws_sdk_controltower.types.enabled_baseline_drift_statuses

        out["inheritanceDriftStatuses"] = (
            aws_sdk_controltower.types.enabled_baseline_drift_statuses.serialize_json(
                value["inheritance_drift_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineFilter:
    out: EnabledBaselineFilter = {}  # type: ignore[typeddict-item]
    if "targetIdentifiers" in data:
        import aws_sdk_controltower.types.enabled_baseline_target_identifiers

        out["target_identifiers"] = (
            aws_sdk_controltower.types.enabled_baseline_target_identifiers.deserialize_json(
                data["targetIdentifiers"]
            )
        )
    if "baselineIdentifiers" in data:
        import aws_sdk_controltower.types.enabled_baseline_baseline_identifiers

        out["baseline_identifiers"] = (
            aws_sdk_controltower.types.enabled_baseline_baseline_identifiers.deserialize_json(
                data["baselineIdentifiers"]
            )
        )
    if "parentIdentifiers" in data:
        import aws_sdk_controltower.types.enabled_baseline_parent_identifiers

        out["parent_identifiers"] = (
            aws_sdk_controltower.types.enabled_baseline_parent_identifiers.deserialize_json(
                data["parentIdentifiers"]
            )
        )
    if "statuses" in data:
        import aws_sdk_controltower.types.enabled_baseline_enablement_statuses

        out["statuses"] = (
            aws_sdk_controltower.types.enabled_baseline_enablement_statuses.deserialize_json(
                data["statuses"]
            )
        )
    if "inheritanceDriftStatuses" in data:
        import aws_sdk_controltower.types.enabled_baseline_drift_statuses

        out["inheritance_drift_statuses"] = (
            aws_sdk_controltower.types.enabled_baseline_drift_statuses.deserialize_json(
                data["inheritanceDriftStatuses"]
            )
        )
    return out
