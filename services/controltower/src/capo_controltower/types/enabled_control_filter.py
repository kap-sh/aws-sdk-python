"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.control_identifiers
    import capo_controltower.types.drift_statuses
    import capo_controltower.types.enablement_statuses
    import capo_controltower.types.parent_identifiers


class EnabledControlFilter(TypedDict, closed=True):
    control_identifiers: NotRequired[
        "capo_controltower.types.control_identifiers.ControlIdentifiers"
    ]
    """<p>The set of <code>controlIdentifier</code> returned by the filter. </p>"""
    statuses: NotRequired[
        "capo_controltower.types.enablement_statuses.EnablementStatuses"
    ]
    """<p>A list of <code>EnablementStatus</code> items.</p>"""
    drift_statuses: NotRequired["capo_controltower.types.drift_statuses.DriftStatuses"]
    """<p>A list of <code>DriftStatus</code> items.</p>"""
    parent_identifiers: NotRequired[
        "capo_controltower.types.parent_identifiers.ParentIdentifiers"
    ]
    """<p>Filters enabled controls by their parent control identifiers, allowing you to find child controls of specific parent controls.</p>"""
    inheritance_drift_statuses: NotRequired[
        "capo_controltower.types.drift_statuses.DriftStatuses"
    ]
    """<p>Filters enabled controls by their inheritance drift status, allowing you to find controls with specific inheritance-related drift conditions.</p>"""
    resource_drift_statuses: NotRequired[
        "capo_controltower.types.drift_statuses.DriftStatuses"
    ]
    """<p>Filters enabled controls by their resource drift status, allowing you to find controls with specific resource-related drift conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlFilter) -> dict:
    out: dict = {}
    if "control_identifiers" in value:
        import capo_controltower.types.control_identifiers

        out["controlIdentifiers"] = (
            capo_controltower.types.control_identifiers.serialize_json(
                value["control_identifiers"]
            )
        )
    if "statuses" in value:
        import capo_controltower.types.enablement_statuses

        out["statuses"] = capo_controltower.types.enablement_statuses.serialize_json(
            value["statuses"]
        )
    if "drift_statuses" in value:
        import capo_controltower.types.drift_statuses

        out["driftStatuses"] = capo_controltower.types.drift_statuses.serialize_json(
            value["drift_statuses"]
        )
    if "parent_identifiers" in value:
        import capo_controltower.types.parent_identifiers

        out["parentIdentifiers"] = (
            capo_controltower.types.parent_identifiers.serialize_json(
                value["parent_identifiers"]
            )
        )
    if "inheritance_drift_statuses" in value:
        import capo_controltower.types.drift_statuses

        out["inheritanceDriftStatuses"] = (
            capo_controltower.types.drift_statuses.serialize_json(
                value["inheritance_drift_statuses"]
            )
        )
    if "resource_drift_statuses" in value:
        import capo_controltower.types.drift_statuses

        out["resourceDriftStatuses"] = (
            capo_controltower.types.drift_statuses.serialize_json(
                value["resource_drift_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledControlFilter:
    out: EnabledControlFilter = {}  # type: ignore[typeddict-item]
    if "controlIdentifiers" in data:
        import capo_controltower.types.control_identifiers

        out["control_identifiers"] = (
            capo_controltower.types.control_identifiers.deserialize_json(
                data["controlIdentifiers"]
            )
        )
    if "statuses" in data:
        import capo_controltower.types.enablement_statuses

        out["statuses"] = capo_controltower.types.enablement_statuses.deserialize_json(
            data["statuses"]
        )
    if "driftStatuses" in data:
        import capo_controltower.types.drift_statuses

        out["drift_statuses"] = capo_controltower.types.drift_statuses.deserialize_json(
            data["driftStatuses"]
        )
    if "parentIdentifiers" in data:
        import capo_controltower.types.parent_identifiers

        out["parent_identifiers"] = (
            capo_controltower.types.parent_identifiers.deserialize_json(
                data["parentIdentifiers"]
            )
        )
    if "inheritanceDriftStatuses" in data:
        import capo_controltower.types.drift_statuses

        out["inheritance_drift_statuses"] = (
            capo_controltower.types.drift_statuses.deserialize_json(
                data["inheritanceDriftStatuses"]
            )
        )
    if "resourceDriftStatuses" in data:
        import capo_controltower.types.drift_statuses

        out["resource_drift_statuses"] = (
            capo_controltower.types.drift_statuses.deserialize_json(
                data["resourceDriftStatuses"]
            )
        )
    return out
