"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPool``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.application_settings_response
    import aws_sdk_workspaces.types.arn
    import aws_sdk_workspaces.types.bundle_id
    import aws_sdk_workspaces.types.capacity_status
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.pools_running_mode
    import aws_sdk_workspaces.types.timeout_settings
    import aws_sdk_workspaces.types.timestamp
    import aws_sdk_workspaces.types.update_description
    import aws_sdk_workspaces.types.workspaces_pool_errors
    import aws_sdk_workspaces.types.workspaces_pool_id
    import aws_sdk_workspaces.types.workspaces_pool_name
    import aws_sdk_workspaces.types.workspaces_pool_state


class WorkspacesPool(TypedDict):
    pool_id: "aws_sdk_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of a pool.</p>"""
    pool_arn: "aws_sdk_workspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the pool.</p>"""
    capacity_status: "aws_sdk_workspaces.types.capacity_status.CapacityStatus"
    """<p>The capacity status for the pool</p>"""
    pool_name: "aws_sdk_workspaces.types.workspaces_pool_name.WorkspacesPoolName"
    """<p>The name of the pool.</p>"""
    description: NotRequired[
        "aws_sdk_workspaces.types.update_description.UpdateDescription"
    ]
    """<p>The description of the pool.</p>"""
    state: "aws_sdk_workspaces.types.workspaces_pool_state.WorkspacesPoolState"
    """<p>The current state of the pool.</p>"""
    created_at: "aws_sdk_workspaces.types.timestamp.Timestamp"
    """<p>The time the pool was created.</p>"""
    bundle_id: "aws_sdk_workspaces.types.bundle_id.BundleId"
    """<p>The identifier of the bundle used by the pool.</p>"""
    directory_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory used by the pool.</p>"""
    errors: NotRequired[
        "aws_sdk_workspaces.types.workspaces_pool_errors.WorkspacesPoolErrors"
    ]
    """<p>The pool errors.</p>"""
    application_settings: NotRequired[
        "aws_sdk_workspaces.types.application_settings_response.ApplicationSettingsResponse"
    ]
    """<p>The persistent application settings for users of the pool.</p>"""
    timeout_settings: NotRequired[
        "aws_sdk_workspaces.types.timeout_settings.TimeoutSettings"
    ]
    """<p>The amount of time that a pool session remains active after users disconnect. If they try to reconnect to the pool session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new pool instance.</p>"""
    running_mode: "aws_sdk_workspaces.types.pools_running_mode.PoolsRunningMode"
    """<p>The running mode of the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPool) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    out["PoolArn"] = value["pool_arn"]
    import aws_sdk_workspaces.types.capacity_status

    out["CapacityStatus"] = (
        aws_sdk_workspaces.types.capacity_status.serialize_aws_json_1_1(
            value["capacity_status"]
        )
    )
    out["PoolName"] = value["pool_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_workspaces.types.workspaces_pool_state

    out["State"] = (
        aws_sdk_workspaces.types.workspaces_pool_state.serialize_aws_json_1_1(
            value["state"]
        )
    )
    import aws_sdk_workspaces.types.timestamp

    out["CreatedAt"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    out["BundleId"] = value["bundle_id"]
    out["DirectoryId"] = value["directory_id"]
    if "errors" in value:
        import aws_sdk_workspaces.types.workspaces_pool_errors

        out["Errors"] = (
            aws_sdk_workspaces.types.workspaces_pool_errors.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    if "application_settings" in value:
        import aws_sdk_workspaces.types.application_settings_response

        out["ApplicationSettings"] = (
            aws_sdk_workspaces.types.application_settings_response.serialize_aws_json_1_1(
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
    import aws_sdk_workspaces.types.pools_running_mode

    out["RunningMode"] = (
        aws_sdk_workspaces.types.pools_running_mode.serialize_aws_json_1_1(
            value.get("running_mode", "AUTO_STOP")
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesPool:
    out: WorkspacesPool = {}  # type: ignore[typeddict-item]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("WorkspacesPool.pool_id required")
    if "PoolArn" in data:
        out["pool_arn"] = data["PoolArn"]
    else:
        raise DeserializationError("WorkspacesPool.pool_arn required")
    if "CapacityStatus" in data:
        import aws_sdk_workspaces.types.capacity_status

        out["capacity_status"] = (
            aws_sdk_workspaces.types.capacity_status.deserialize_aws_json_1_1(
                data["CapacityStatus"]
            )
        )
    else:
        raise DeserializationError("WorkspacesPool.capacity_status required")
    if "PoolName" in data:
        out["pool_name"] = data["PoolName"]
    else:
        raise DeserializationError("WorkspacesPool.pool_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import aws_sdk_workspaces.types.workspaces_pool_state

        out["state"] = (
            aws_sdk_workspaces.types.workspaces_pool_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    else:
        raise DeserializationError("WorkspacesPool.state required")
    if "CreatedAt" in data:
        import aws_sdk_workspaces.types.timestamp

        out["created_at"] = aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("WorkspacesPool.created_at required")
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    else:
        raise DeserializationError("WorkspacesPool.bundle_id required")
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("WorkspacesPool.directory_id required")
    if "Errors" in data:
        import aws_sdk_workspaces.types.workspaces_pool_errors

        out["errors"] = (
            aws_sdk_workspaces.types.workspaces_pool_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    if "ApplicationSettings" in data:
        import aws_sdk_workspaces.types.application_settings_response

        out["application_settings"] = (
            aws_sdk_workspaces.types.application_settings_response.deserialize_aws_json_1_1(
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
    else:
        out["running_mode"] = "AUTO_STOP"
    return out
