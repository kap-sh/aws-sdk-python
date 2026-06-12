"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspacesPoolRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.application_settings_request
    import aws_sdk_workspaces.types.bundle_id
    import aws_sdk_workspaces.types.capacity
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.pools_running_mode
    import aws_sdk_workspaces.types.tag_list
    import aws_sdk_workspaces.types.timeout_settings
    import aws_sdk_workspaces.types.update_description
    import aws_sdk_workspaces.types.workspaces_pool_name


class CreateWorkspacesPoolRequest(TypedDict):
    pool_name: "aws_sdk_workspaces.types.workspaces_pool_name.WorkspacesPoolName"
    """<p>The name of the pool.</p>"""
    description: "aws_sdk_workspaces.types.update_description.UpdateDescription"
    """<p>The pool description.</p>"""
    bundle_id: "aws_sdk_workspaces.types.bundle_id.BundleId"
    """<p>The identifier of the bundle for the pool.</p>"""
    directory_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for the pool.</p>"""
    capacity: "aws_sdk_workspaces.types.capacity.Capacity"
    """<p>The user capacity of the pool.</p>"""
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags for the pool.</p>"""
    application_settings: NotRequired[
        "aws_sdk_workspaces.types.application_settings_request.ApplicationSettingsRequest"
    ]
    """<p>Indicates the application settings of the pool.</p>"""
    timeout_settings: NotRequired[
        "aws_sdk_workspaces.types.timeout_settings.TimeoutSettings"
    ]
    """<p>Indicates the timeout settings of the pool.</p>"""
    running_mode: NotRequired[
        "aws_sdk_workspaces.types.pools_running_mode.PoolsRunningMode"
    ]
    """<p>The running mode for the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolName"] = value["pool_name"]
    out["Description"] = value["description"]
    out["BundleId"] = value["bundle_id"]
    out["DirectoryId"] = value["directory_id"]
    import aws_sdk_workspaces.types.capacity

    out["Capacity"] = aws_sdk_workspaces.types.capacity.serialize_aws_json_1_1(
        value["capacity"]
    )
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "application_settings" in value:
        import aws_sdk_workspaces.types.application_settings_request

        out["ApplicationSettings"] = (
            aws_sdk_workspaces.types.application_settings_request.serialize_aws_json_1_1(
                value["application_settings"]
            )
        )
    if "timeout_settings" in value:
        import aws_sdk_workspaces.types.timeout_settings

        out["TimeoutSettings"] = (
            aws_sdk_workspaces.types.timeout_settings.serialize_aws_json_1_1(
                value["timeout_settings"]
            )
        )
    if "running_mode" in value:
        import aws_sdk_workspaces.types.pools_running_mode

        out["RunningMode"] = (
            aws_sdk_workspaces.types.pools_running_mode.serialize_aws_json_1_1(
                value["running_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspacesPoolRequest:
    out: CreateWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if "PoolName" in data:
        out["pool_name"] = data["PoolName"]
    else:
        raise DeserializationError("CreateWorkspacesPoolRequest.pool_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateWorkspacesPoolRequest.description required")
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    else:
        raise DeserializationError("CreateWorkspacesPoolRequest.bundle_id required")
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("CreateWorkspacesPoolRequest.directory_id required")
    if "Capacity" in data:
        import aws_sdk_workspaces.types.capacity

        out["capacity"] = aws_sdk_workspaces.types.capacity.deserialize_aws_json_1_1(
            data["Capacity"]
        )
    else:
        raise DeserializationError("CreateWorkspacesPoolRequest.capacity required")
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ApplicationSettings" in data:
        import aws_sdk_workspaces.types.application_settings_request

        out["application_settings"] = (
            aws_sdk_workspaces.types.application_settings_request.deserialize_aws_json_1_1(
                data["ApplicationSettings"]
            )
        )
    if "TimeoutSettings" in data:
        import aws_sdk_workspaces.types.timeout_settings

        out["timeout_settings"] = (
            aws_sdk_workspaces.types.timeout_settings.deserialize_aws_json_1_1(
                data["TimeoutSettings"]
            )
        )
    if "RunningMode" in data:
        import aws_sdk_workspaces.types.pools_running_mode

        out["running_mode"] = (
            aws_sdk_workspaces.types.pools_running_mode.deserialize_aws_json_1_1(
                data["RunningMode"]
            )
        )
    return out
