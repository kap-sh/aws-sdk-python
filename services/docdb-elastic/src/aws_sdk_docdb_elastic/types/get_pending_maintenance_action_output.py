"""Generated from Smithy shape ``com.amazonaws.docdbelastic#GetPendingMaintenanceActionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action


class GetPendingMaintenanceActionOutput(TypedDict, closed=True):
    resource_pending_maintenance_action: "aws_sdk_docdb_elastic.types.resource_pending_maintenance_action.ResourcePendingMaintenanceAction"
    """<p>Provides information about a pending maintenance action for a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPendingMaintenanceActionOutput) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action

    out["resourcePendingMaintenanceAction"] = (
        aws_sdk_docdb_elastic.types.resource_pending_maintenance_action.serialize_json(
            value["resource_pending_maintenance_action"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPendingMaintenanceActionOutput:
    out: GetPendingMaintenanceActionOutput = {}  # type: ignore[typeddict-item]
    if "resourcePendingMaintenanceAction" in data:
        import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action

        out["resource_pending_maintenance_action"] = (
            aws_sdk_docdb_elastic.types.resource_pending_maintenance_action.deserialize_json(
                data["resourcePendingMaintenanceAction"]
            )
        )
    else:
        raise DeserializationError(
            "GetPendingMaintenanceActionOutput.resource_pending_maintenance_action required"
        )
    return out
