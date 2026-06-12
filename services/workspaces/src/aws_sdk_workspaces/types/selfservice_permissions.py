"""Generated from Smithy shape ``com.amazonaws.workspaces#SelfservicePermissions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.reconnect_enum


class SelfservicePermissions(TypedDict):
    restart_workspace: NotRequired[
        "aws_sdk_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can restart their WorkSpace.</p>"""
    increase_volume_size: NotRequired[
        "aws_sdk_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can increase the volume size of the drives on their WorkSpace.</p>"""
    change_compute_type: NotRequired[
        "aws_sdk_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can change the compute type (bundle) for their WorkSpace.</p>"""
    switch_running_mode: NotRequired[
        "aws_sdk_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can switch the running mode of their WorkSpace.</p>"""
    rebuild_workspace: NotRequired[
        "aws_sdk_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can rebuild the operating system of a WorkSpace to its original state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelfservicePermissions) -> dict:
    out: dict = {}
    if "restart_workspace" in value:
        import aws_sdk_workspaces.types.reconnect_enum

        out["RestartWorkspace"] = (
            aws_sdk_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["restart_workspace"]
            )
        )
    if "increase_volume_size" in value:
        import aws_sdk_workspaces.types.reconnect_enum

        out["IncreaseVolumeSize"] = (
            aws_sdk_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["increase_volume_size"]
            )
        )
    if "change_compute_type" in value:
        import aws_sdk_workspaces.types.reconnect_enum

        out["ChangeComputeType"] = (
            aws_sdk_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["change_compute_type"]
            )
        )
    if "switch_running_mode" in value:
        import aws_sdk_workspaces.types.reconnect_enum

        out["SwitchRunningMode"] = (
            aws_sdk_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["switch_running_mode"]
            )
        )
    if "rebuild_workspace" in value:
        import aws_sdk_workspaces.types.reconnect_enum

        out["RebuildWorkspace"] = (
            aws_sdk_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["rebuild_workspace"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SelfservicePermissions:
    out: SelfservicePermissions = {}  # type: ignore[typeddict-item]
    if "RestartWorkspace" in data:
        import aws_sdk_workspaces.types.reconnect_enum

        out["restart_workspace"] = (
            aws_sdk_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["RestartWorkspace"]
            )
        )
    if "IncreaseVolumeSize" in data:
        import aws_sdk_workspaces.types.reconnect_enum

        out["increase_volume_size"] = (
            aws_sdk_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["IncreaseVolumeSize"]
            )
        )
    if "ChangeComputeType" in data:
        import aws_sdk_workspaces.types.reconnect_enum

        out["change_compute_type"] = (
            aws_sdk_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["ChangeComputeType"]
            )
        )
    if "SwitchRunningMode" in data:
        import aws_sdk_workspaces.types.reconnect_enum

        out["switch_running_mode"] = (
            aws_sdk_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["SwitchRunningMode"]
            )
        )
    if "RebuildWorkspace" in data:
        import aws_sdk_workspaces.types.reconnect_enum

        out["rebuild_workspace"] = (
            aws_sdk_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["RebuildWorkspace"]
            )
        )
    return out
