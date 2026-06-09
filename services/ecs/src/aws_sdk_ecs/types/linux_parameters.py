"""Generated from Smithy shape ``com.amazonaws.ecs#LinuxParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.devices_list
    import aws_sdk_ecs.types.kernel_capabilities
    import aws_sdk_ecs.types.tmpfs_list


class LinuxParameters(TypedDict):
    capabilities: NotRequired[
        "aws_sdk_ecs.types.kernel_capabilities.KernelCapabilities"
    ]
    """<p>The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.</p> <note> <p>For tasks that use the Fargate launch type, <code>capabilities</code> is supported for all platform versions but the <code>add</code> parameter is only supported if using platform version 1.4.0 or later.</p> </note>"""
    devices: NotRequired["aws_sdk_ecs.types.devices_list.DevicesList"]
    """<p>Any host devices to expose to the container. This parameter maps to <code>Devices</code> in the docker container create command and the <code>--device</code> option to docker run.</p> <note> <p>If you're using tasks that use the Fargate launch type, the <code>devices</code> parameter isn't supported.</p> </note>"""
    init_process_enabled: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Run an <code>init</code> process inside the container that forwards signals and reaps processes. This parameter maps to the <code>--init</code> option to docker run. This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version --format '{{.Server.APIVersion}}'</code> </p>"""
    shared_memory_size: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The value for the size (in MiB) of the <code>/dev/shm</code> volume. This parameter maps to the <code>--shm-size</code> option to docker run.</p> <note> <p>If you are using tasks that use the Fargate launch type, the <code>sharedMemorySize</code> parameter is not supported.</p> </note>"""
    tmpfs: NotRequired["aws_sdk_ecs.types.tmpfs_list.TmpfsList"]
    """<p>The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the <code>--tmpfs</code> option to docker run.</p>"""
    max_swap: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The total amount of swap memory (in MiB) a container can use. This parameter will be translated to the <code>--memory-swap</code> option to docker run where the value would be the sum of the container memory plus the <code>maxSwap</code> value.</p> <p>If a <code>maxSwap</code> value of <code>0</code> is specified, the container will not use swap. Accepted values are <code>0</code> or any positive integer. If the <code>maxSwap</code> parameter is omitted, the container will use the swap configuration for the container instance it is running on. A <code>maxSwap</code> value must be set for the <code>swappiness</code> parameter to be used.</p> <note> <p>If you're using tasks that use the Fargate launch type, the <code>maxSwap</code> parameter isn't supported.</p> <p>If you're using tasks on Amazon Linux 2023 the <code>swappiness</code> parameter isn't supported.</p> </note>"""
    swappiness: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>This allows you to tune a container's memory swappiness behavior. A <code>swappiness</code> value of <code>0</code> will cause swapping to not happen unless absolutely necessary. A <code>swappiness</code> value of <code>100</code> will cause pages to be swapped very aggressively. Accepted values are whole numbers between <code>0</code> and <code>100</code>. If the <code>swappiness</code> parameter is not specified, a default value of <code>60</code> is used. If a value is not specified for <code>maxSwap</code> then this parameter is ignored. This parameter maps to the <code>--memory-swappiness</code> option to docker run.</p> <note> <p>If you're using tasks that use the Fargate launch type, the <code>swappiness</code> parameter isn't supported.</p> <p>If you're using tasks on Amazon Linux 2023 the <code>swappiness</code> parameter isn't supported.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LinuxParameters) -> dict:
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
    if "shared_memory_size" in value:
        out["sharedMemorySize"] = value["shared_memory_size"]
    if "tmpfs" in value:
        import aws_sdk_ecs.types.tmpfs_list

        out["tmpfs"] = aws_sdk_ecs.types.tmpfs_list.serialize_aws_json_1_1(
            value["tmpfs"]
        )
    if "max_swap" in value:
        out["maxSwap"] = value["max_swap"]
    if "swappiness" in value:
        out["swappiness"] = value["swappiness"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LinuxParameters:
    out: LinuxParameters = {}  # type: ignore[typeddict-item]
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
    if "sharedMemorySize" in data:
        out["shared_memory_size"] = data["sharedMemorySize"]
    if "tmpfs" in data:
        import aws_sdk_ecs.types.tmpfs_list

        out["tmpfs"] = aws_sdk_ecs.types.tmpfs_list.deserialize_aws_json_1_1(
            data["tmpfs"]
        )
    if "maxSwap" in data:
        out["max_swap"] = data["maxSwap"]
    if "swappiness" in data:
        out["swappiness"] = data["swappiness"]
    return out
