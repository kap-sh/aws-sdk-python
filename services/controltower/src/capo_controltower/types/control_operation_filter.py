"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.control_identifiers
    import capo_controltower.types.control_operation_statuses
    import capo_controltower.types.control_operation_types
    import capo_controltower.types.enabled_control_identifiers
    import capo_controltower.types.target_identifiers


class ControlOperationFilter(TypedDict, closed=True):
    control_identifiers: NotRequired[
        "capo_controltower.types.control_identifiers.ControlIdentifiers"
    ]
    """<p>The set of <code>controlIdentifier</code> returned by the filter.</p>"""
    target_identifiers: NotRequired[
        "capo_controltower.types.target_identifiers.TargetIdentifiers"
    ]
    """<p>The set of <code>targetIdentifier</code> objects returned by the filter.</p>"""
    enabled_control_identifiers: NotRequired[
        "capo_controltower.types.enabled_control_identifiers.EnabledControlIdentifiers"
    ]
    """<p>The set <code>controlIdentifier</code> of enabled controls selected by the filter.</p>"""
    statuses: NotRequired[
        "capo_controltower.types.control_operation_statuses.ControlOperationStatuses"
    ]
    """<p>Lists the status of control operations.</p>"""
    control_operation_types: NotRequired[
        "capo_controltower.types.control_operation_types.ControlOperationTypes"
    ]
    """<p>The set of <code>ControlOperation</code> objects returned by the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlOperationFilter) -> dict:
    out: dict = {}
    if "control_identifiers" in value:
        import capo_controltower.types.control_identifiers

        out["controlIdentifiers"] = (
            capo_controltower.types.control_identifiers.serialize_json(
                value["control_identifiers"]
            )
        )
    if "target_identifiers" in value:
        import capo_controltower.types.target_identifiers

        out["targetIdentifiers"] = (
            capo_controltower.types.target_identifiers.serialize_json(
                value["target_identifiers"]
            )
        )
    if "enabled_control_identifiers" in value:
        import capo_controltower.types.enabled_control_identifiers

        out["enabledControlIdentifiers"] = (
            capo_controltower.types.enabled_control_identifiers.serialize_json(
                value["enabled_control_identifiers"]
            )
        )
    if "statuses" in value:
        import capo_controltower.types.control_operation_statuses

        out["statuses"] = (
            capo_controltower.types.control_operation_statuses.serialize_json(
                value["statuses"]
            )
        )
    if "control_operation_types" in value:
        import capo_controltower.types.control_operation_types

        out["controlOperationTypes"] = (
            capo_controltower.types.control_operation_types.serialize_json(
                value["control_operation_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlOperationFilter:
    out: ControlOperationFilter = {}  # type: ignore[typeddict-item]
    if "controlIdentifiers" in data:
        import capo_controltower.types.control_identifiers

        out["control_identifiers"] = (
            capo_controltower.types.control_identifiers.deserialize_json(
                data["controlIdentifiers"]
            )
        )
    if "targetIdentifiers" in data:
        import capo_controltower.types.target_identifiers

        out["target_identifiers"] = (
            capo_controltower.types.target_identifiers.deserialize_json(
                data["targetIdentifiers"]
            )
        )
    if "enabledControlIdentifiers" in data:
        import capo_controltower.types.enabled_control_identifiers

        out["enabled_control_identifiers"] = (
            capo_controltower.types.enabled_control_identifiers.deserialize_json(
                data["enabledControlIdentifiers"]
            )
        )
    if "statuses" in data:
        import capo_controltower.types.control_operation_statuses

        out["statuses"] = (
            capo_controltower.types.control_operation_statuses.deserialize_json(
                data["statuses"]
            )
        )
    if "controlOperationTypes" in data:
        import capo_controltower.types.control_operation_types

        out["control_operation_types"] = (
            capo_controltower.types.control_operation_types.deserialize_json(
                data["controlOperationTypes"]
            )
        )
    return out
