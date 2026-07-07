"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ListPendingMaintenanceActionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.pagination_token
    import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action_list


class ListPendingMaintenanceActionsOutput(TypedDict, closed=True):
    resource_pending_maintenance_actions: "aws_sdk_docdb_elastic.types.resource_pending_maintenance_action_list.ResourcePendingMaintenanceActionList"
    """<p>Provides information about a pending maintenance action for a resource.</p>"""
    next_token: NotRequired[
        "aws_sdk_docdb_elastic.types.pagination_token.PaginationToken"
    ]
    """<p>An optional pagination token provided by a previous request. If this parameter is displayed, the responses will include only records beyond the marker, up to the value specified by <code>maxResults</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingMaintenanceActionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action_list

    out["resourcePendingMaintenanceActions"] = (
        aws_sdk_docdb_elastic.types.resource_pending_maintenance_action_list.serialize_json(
            value["resource_pending_maintenance_actions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPendingMaintenanceActionsOutput:
    out: ListPendingMaintenanceActionsOutput = {}  # type: ignore[typeddict-item]
    if "resourcePendingMaintenanceActions" in data:
        import aws_sdk_docdb_elastic.types.resource_pending_maintenance_action_list

        out["resource_pending_maintenance_actions"] = (
            aws_sdk_docdb_elastic.types.resource_pending_maintenance_action_list.deserialize_json(
                data["resourcePendingMaintenanceActions"]
            )
        )
    else:
        raise DeserializationError(
            "ListPendingMaintenanceActionsOutput.resource_pending_maintenance_actions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
