"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ApplyPendingMaintenanceActionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import capo_docdb_elastic.types.resource_pending_maintenance_action


class ApplyPendingMaintenanceActionOutput(TypedDict, closed=True):
    resource_pending_maintenance_action: "capo_docdb_elastic.types.resource_pending_maintenance_action.ResourcePendingMaintenanceAction"
    """<p>The output of the pending maintenance action being applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplyPendingMaintenanceActionOutput) -> dict:
    out: dict = {}
    import capo_docdb_elastic.types.resource_pending_maintenance_action

    out["resourcePendingMaintenanceAction"] = (
        capo_docdb_elastic.types.resource_pending_maintenance_action.serialize_json(
            value["resource_pending_maintenance_action"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApplyPendingMaintenanceActionOutput:
    out: ApplyPendingMaintenanceActionOutput = {}  # type: ignore[typeddict-item]
    if "resourcePendingMaintenanceAction" in data:
        import capo_docdb_elastic.types.resource_pending_maintenance_action

        out["resource_pending_maintenance_action"] = (
            capo_docdb_elastic.types.resource_pending_maintenance_action.deserialize_json(
                data["resourcePendingMaintenanceAction"]
            )
        )
    else:
        raise DeserializationError(
            "ApplyPendingMaintenanceActionOutput.resource_pending_maintenance_action required"
        )
    return out
