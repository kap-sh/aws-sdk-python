"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppPermissionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.permissions_input_list
    import capo_qapps.types.uuid


class UpdateQAppPermissionsInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Amazon Q App for which permissions are being updated.</p>"""
    grant_permissions: NotRequired[
        "capo_qapps.types.permissions_input_list.PermissionsInputList"
    ]
    """<p>The list of permissions to grant for the Amazon Q App.</p>"""
    revoke_permissions: NotRequired[
        "capo_qapps.types.permissions_input_list.PermissionsInputList"
    ]
    """<p>The list of permissions to revoke for the Amazon Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppPermissionsInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    if "grant_permissions" in value:
        import capo_qapps.types.permissions_input_list

        out["grantPermissions"] = (
            capo_qapps.types.permissions_input_list.serialize_json(
                value["grant_permissions"]
            )
        )
    if "revoke_permissions" in value:
        import capo_qapps.types.permissions_input_list

        out["revokePermissions"] = (
            capo_qapps.types.permissions_input_list.serialize_json(
                value["revoke_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateQAppPermissionsInput:
    out: UpdateQAppPermissionsInput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("UpdateQAppPermissionsInput.app_id required")
    if "grantPermissions" in data:
        import capo_qapps.types.permissions_input_list

        out["grant_permissions"] = (
            capo_qapps.types.permissions_input_list.deserialize_json(
                data["grantPermissions"]
            )
        )
    if "revokePermissions" in data:
        import capo_qapps.types.permissions_input_list

        out["revoke_permissions"] = (
            capo_qapps.types.permissions_input_list.deserialize_json(
                data["revokePermissions"]
            )
        )
    return out
