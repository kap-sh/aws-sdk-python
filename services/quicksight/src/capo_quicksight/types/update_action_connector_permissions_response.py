"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateActionConnectorPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code


class UpdateActionConnectorPermissionsResponse(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the action connector.</p>"""
    action_connector_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The unique identifier of the action connector.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status code of the request.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The updated permissions configuration for the action connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionConnectorPermissionsResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "action_connector_id" in value:
        out["ActionConnectorId"] = value["action_connector_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateActionConnectorPermissionsResponse:
    out: UpdateActionConnectorPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ActionConnectorId" in data:
        out["action_connector_id"] = data["ActionConnectorId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Permissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    return out
