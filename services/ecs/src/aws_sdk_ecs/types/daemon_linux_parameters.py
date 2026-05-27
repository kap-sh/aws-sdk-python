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
