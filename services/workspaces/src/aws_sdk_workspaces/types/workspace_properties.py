"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.compute
    import aws_sdk_workspaces.types.global_accelerator_for_work_space
    import aws_sdk_workspaces.types.operating_system_name
    import aws_sdk_workspaces.types.protocol_list
    import aws_sdk_workspaces.types.root_volume_size_gib
    import aws_sdk_workspaces.types.running_mode
    import aws_sdk_workspaces.types.running_mode_auto_stop_timeout_in_minutes
    import aws_sdk_workspaces.types.user_volume_size_gib


class WorkspaceProperties(TypedDict):
    running_mode: NotRequired["aws_sdk_workspaces.types.running_mode.RunningMode"]
    r"""<p>The running mode. For more information, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html\">Manage the WorkSpace Running Mode</a>.</p> <note> <p>The <code>MANUAL</code> value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see <a href=\"http://aws.amazon.com/workspaces/core/\">Amazon WorkSpaces Core</a>.</p> </note> <p>Review your running mode to ensure you are using one that is optimal for your needs and budget. For more information on switching running modes, see <a href=\"http://aws.amazon.com/workspaces-family/workspaces/faqs/#:~:text=Can%20I%20switch%20between%20hourly%20and%20monthly%20billing%20on%20WorkSpaces%20Personal%3F\"> Can I switch between hourly and monthly billing?</a> </p>"""
    running_mode_auto_stop_timeout_in_minutes: NotRequired[
        "aws_sdk_workspaces.types.running_mode_auto_stop_timeout_in_minutes.RunningModeAutoStopTimeoutInMinutes"
    ]
    """<p>The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.</p>"""
    root_volume_size_gib: NotRequired[
        "aws_sdk_workspaces.types.root_volume_size_gib.RootVolumeSizeGib"
    ]
    r"""<p>The size of the root volume. For important information about how to modify the size of the root and user volumes, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html\">Modify a WorkSpace</a>.</p>"""
    user_volume_size_gib: NotRequired[
        "aws_sdk_workspaces.types.user_volume_size_gib.UserVolumeSizeGib"
    ]
    r"""<p>The size of the user storage. For important information about how to modify the size of the root and user volumes, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html\">Modify a WorkSpace</a>.</p>"""
    compute_type_name: NotRequired["aws_sdk_workspaces.types.compute.Compute"]
    r"""<p>The compute type. For more information, see <a href=\"http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles\">Amazon WorkSpaces Bundles</a>.</p>"""
    protocols: NotRequired["aws_sdk_workspaces.types.protocol_list.ProtocolList"]
    r"""<p>The protocol. For more information, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-protocols.html\"> Protocols for Amazon WorkSpaces</a>.</p> <note> <ul> <li> <p>Only available for WorkSpaces created with PCoIP bundles.</p> </li> <li> <p>The <code>Protocols</code> property is case sensitive. Ensure you use <code>PCOIP</code> or <code>DCV</code> (formerly WSP).</p> </li> <li> <p>Unavailable for Windows 7 WorkSpaces and WorkSpaces using GPU-based bundles (Graphics, GraphicsPro, Graphics.g4dn, and GraphicsPro.g4dn).</p> </li> </ul> </note>"""
    operating_system_name: NotRequired[
        "aws_sdk_workspaces.types.operating_system_name.OperatingSystemName"
    ]
    """<p>The name of the operating system.</p>"""
    global_accelerator: NotRequired[
        "aws_sdk_workspaces.types.global_accelerator_for_work_space.GlobalAcceleratorForWorkSpace"
    ]
    """<p>Indicates the Global Accelerator properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceProperties) -> dict:
    out: dict = {}
    if "running_mode" in value:
        import aws_sdk_workspaces.types.running_mode

        out["RunningMode"] = (
            aws_sdk_workspaces.types.running_mode.serialize_aws_json_1_1(
                value["running_mode"]
            )
        )
    if "running_mode_auto_stop_timeout_in_minutes" in value:
        out["RunningModeAutoStopTimeoutInMinutes"] = value[
            "running_mode_auto_stop_timeout_in_minutes"
        ]
    if "root_volume_size_gib" in value:
        out["RootVolumeSizeGib"] = value["root_volume_size_gib"]
    if "user_volume_size_gib" in value:
        out["UserVolumeSizeGib"] = value["user_volume_size_gib"]
    if "compute_type_name" in value:
        import aws_sdk_workspaces.types.compute

        out["ComputeTypeName"] = (
            aws_sdk_workspaces.types.compute.serialize_aws_json_1_1(
                value["compute_type_name"]
            )
        )
    if "protocols" in value:
        import aws_sdk_workspaces.types.protocol_list

        out["Protocols"] = (
            aws_sdk_workspaces.types.protocol_list.serialize_aws_json_1_1(
                value["protocols"]
            )
        )
    if "operating_system_name" in value:
        import aws_sdk_workspaces.types.operating_system_name

        out["OperatingSystemName"] = (
            aws_sdk_workspaces.types.operating_system_name.serialize_aws_json_1_1(
                value["operating_system_name"]
            )
        )
    if "global_accelerator" in value:
        import aws_sdk_workspaces.types.global_accelerator_for_work_space

        out["GlobalAccelerator"] = (
            aws_sdk_workspaces.types.global_accelerator_for_work_space.serialize_aws_json_1_1(
                value["global_accelerator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceProperties:
    out: WorkspaceProperties = {}  # type: ignore[typeddict-item]
    if "RunningMode" in data:
        import aws_sdk_workspaces.types.running_mode

        out["running_mode"] = (
            aws_sdk_workspaces.types.running_mode.deserialize_aws_json_1_1(
                data["RunningMode"]
            )
        )
    if "RunningModeAutoStopTimeoutInMinutes" in data:
        out["running_mode_auto_stop_timeout_in_minutes"] = data[
            "RunningModeAutoStopTimeoutInMinutes"
        ]
    if "RootVolumeSizeGib" in data:
        out["root_volume_size_gib"] = data["RootVolumeSizeGib"]
    if "UserVolumeSizeGib" in data:
        out["user_volume_size_gib"] = data["UserVolumeSizeGib"]
    if "ComputeTypeName" in data:
        import aws_sdk_workspaces.types.compute

        out["compute_type_name"] = (
            aws_sdk_workspaces.types.compute.deserialize_aws_json_1_1(
                data["ComputeTypeName"]
            )
        )
    if "Protocols" in data:
        import aws_sdk_workspaces.types.protocol_list

        out["protocols"] = (
            aws_sdk_workspaces.types.protocol_list.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    if "OperatingSystemName" in data:
        import aws_sdk_workspaces.types.operating_system_name

        out["operating_system_name"] = (
            aws_sdk_workspaces.types.operating_system_name.deserialize_aws_json_1_1(
                data["OperatingSystemName"]
            )
        )
    if "GlobalAccelerator" in data:
        import aws_sdk_workspaces.types.global_accelerator_for_work_space

        out["global_accelerator"] = (
            aws_sdk_workspaces.types.global_accelerator_for_work_space.deserialize_aws_json_1_1(
                data["GlobalAccelerator"]
            )
        )
    return out
