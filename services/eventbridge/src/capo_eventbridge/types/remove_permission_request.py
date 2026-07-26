"""Generated from Smithy shape ``com.amazonaws.eventbridge#RemovePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.boolean
    import capo_eventbridge.types.non_partner_event_bus_name
    import capo_eventbridge.types.statement_id


class RemovePermissionRequest(TypedDict, closed=True):
    statement_id: NotRequired["capo_eventbridge.types.statement_id.StatementId"]
    """<p>The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.</p>"""
    remove_all_permissions: "capo_eventbridge.types.boolean.Boolean"
    """<p>Specifies whether to remove all permissions.</p>"""
    event_bus_name: NotRequired[
        "capo_eventbridge.types.non_partner_event_bus_name.NonPartnerEventBusName"
    ]
    """<p>The name of the event bus to revoke permissions for. If you omit this, the default event bus is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemovePermissionRequest) -> dict:
    out: dict = {}
    if "statement_id" in value:
        out["StatementId"] = value["statement_id"]
    out["RemoveAllPermissions"] = value.get("remove_all_permissions", False)
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemovePermissionRequest:
    out: RemovePermissionRequest = {}  # type: ignore[typeddict-item]
    if "StatementId" in data:
        out["statement_id"] = data["StatementId"]
    if "RemoveAllPermissions" in data:
        out["remove_all_permissions"] = data["RemoveAllPermissions"]
    else:
        out["remove_all_permissions"] = False
    if "EventBusName" in data:
        out["event_bus_name"] = data["EventBusName"]
    return out
