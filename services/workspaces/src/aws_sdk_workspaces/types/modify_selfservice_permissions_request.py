"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifySelfservicePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.selfservice_permissions


class ModifySelfservicePermissionsRequest(TypedDict):
    resource_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    selfservice_permissions: (
        "aws_sdk_workspaces.types.selfservice_permissions.SelfservicePermissions"
    )
    """<p>The permissions to enable or disable self-service capabilities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifySelfservicePermissionsRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_workspaces.types.selfservice_permissions

    out["SelfservicePermissions"] = (
        aws_sdk_workspaces.types.selfservice_permissions.serialize_aws_json_1_1(
            value["selfservice_permissions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifySelfservicePermissionsRequest:
    out: ModifySelfservicePermissionsRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "ModifySelfservicePermissionsRequest.resource_id required"
        )
    if "SelfservicePermissions" in data:
        import aws_sdk_workspaces.types.selfservice_permissions

        out["selfservice_permissions"] = (
            aws_sdk_workspaces.types.selfservice_permissions.deserialize_aws_json_1_1(
                data["SelfservicePermissions"]
            )
        )
    else:
        raise DeserializationError(
            "ModifySelfservicePermissionsRequest.selfservice_permissions required"
        )
    return out
