"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateWorkspacesPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.application_settings_request
    import aws_sdk_workspaces.types.bundle_id
    import aws_sdk_workspaces.types.capacity
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.pools_running_mode
    import aws_sdk_workspaces.types.timeout_settings
    import aws_sdk_workspaces.types.update_description
    import aws_sdk_workspaces.types.workspaces_pool_id


class UpdateWorkspacesPoolRequest(TypedDict, closed=True):
    pool_id: "aws_sdk_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the specified pool to update.</p>"""
    description: NotRequired[
        "aws_sdk_workspaces.types.update_description.UpdateDescription"
    ]
    """<p>Describes the specified pool to update.</p>"""
    bundle_id: NotRequired["aws_sdk_workspaces.types.bundle_id.BundleId"]
    """<p>The identifier of the bundle.</p>"""
    directory_id: NotRequired["aws_sdk_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory.</p>"""
    capacity: NotRequired["aws_sdk_workspaces.types.capacity.Capacity"]
    """<p>The desired capacity for the pool.</p>"""
    application_settings: NotRequired[
        "aws_sdk_workspaces.types.application_settings_request.ApplicationSettingsRequest"
    ]
    """<p>The persistent application settings for users in the pool.</p>"""
    timeout_settings: NotRequired[
        "aws_sdk_workspaces.types.timeout_settings.TimeoutSettings"
    ]
    """<p>Indicates the timeout settings of the specified pool.</p>"""
    running_mode: NotRequired[
        "aws_sdk_workspaces.types.pools_running_mode.PoolsRunningMode"
    ]
    """<p>The desired running mode for the pool. The running mode can only be updated when the pool is in a stopped state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "bundle_id" in value:
        out["BundleId"] = value["bundle_id"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "capacity" in value:
        import aws_sdk_workspaces.types.capacity

        out["Capacity"] = aws_sdk_workspaces.types.capacity.serialize_aws_json_1_1(
            value["capacity"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkspacesPoolRequest:
    out: UpdateWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("UpdateWorkspacesPoolRequest.pool_id required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "Capacity" in data:
        import aws_sdk_workspaces.types.capacity

        out["capacity"] = aws_sdk_workspaces.types.capacity.deserialize_aws_json_1_1(
            data["Capacity"]
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
