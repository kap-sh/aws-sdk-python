"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonLinuxParameters``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.devices_list
    import aws_sdk_ecs.types.kernel_capabilities
    import aws_sdk_ecs.types.tmpfs_list


class DaemonLinuxParameters(TypedDict):
    capabilities: NotRequired[
        "aws_sdk_ecs.types.kernel_capabilities.KernelCapabilities"
    ]
    """<p>The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.</p>"""
    devices: NotRequired["aws_sdk_ecs.types.devices_list.DevicesList"]
    """<p>Any host devices to expose to the container.</p>"""
    init_process_enabled: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Run an <code>init</code> process inside the container that forwards signals and reaps processes.</p>"""
    tmpfs: NotRequired["aws_sdk_ecs.types.tmpfs_list.TmpfsList"]
    """<p>The container path, mount options, and size (in MiB) of the tmpfs mount.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonLinuxParameters) -> dict:
    out: dict = {}
    if "capabilities" in value:
        import aws_sdk_ecs.types.kernel_capabilities

        out["capabilities"] = (
            aws_sdk_ecs.types.kernel_capabilities.serialize_aws_json_1_1(
                value["capabilities"]
            )
        )
    if "devices" in value:
        import aws_sdk_ecs.types.devices_list

        out["devices"] = aws_sdk_ecs.types.devices_list.serialize_aws_json_1_1(
            value["devices"]
        )
    if "init_process_enabled" in value:
        out["initProcessEnabled"] = value["init_process_enabled"]
    if "tmpfs" in value:
        import aws_sdk_ecs.types.tmpfs_list

        out["tmpfs"] = aws_sdk_ecs.types.tmpfs_list.serialize_aws_json_1_1(
            value["tmpfs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonLinuxParameters:
    out: DaemonLinuxParameters = {}  # type: ignore[typeddict-item]
    if "capabilities" in data:
        import aws_sdk_ecs.types.kernel_capabilities

        out["capabilities"] = (
            aws_sdk_ecs.types.kernel_capabilities.deserialize_aws_json_1_1(
                data["capabilities"]
            )
        )
    if "devices" in data:
        import aws_sdk_ecs.types.devices_list

        out["devices"] = aws_sdk_ecs.types.devices_list.deserialize_aws_json_1_1(
            data["devices"]
        )
    if "initProcessEnabled" in data:
        out["init_process_enabled"] = data["initProcessEnabled"]
    if "tmpfs" in data:
        import aws_sdk_ecs.types.tmpfs_list

        out["tmpfs"] = aws_sdk_ecs.types.tmpfs_list.deserialize_aws_json_1_1(
            data["tmpfs"]
        )
    return out
