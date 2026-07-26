"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_capabilities_details
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails(
    TypedDict, closed=True
):
    capabilities: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_capabilities_details.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails"
    ]
    """<p>The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.</p>"""
    devices: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_list.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesList"
    ]
    """<p>The host devices to expose to the container.</p>"""
    init_process_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to run an <code>init</code> process inside the container that forwards signals and reaps processes. </p>"""
    max_swap: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The total amount of swap memory (in MiB) that a container can use.</p>"""
    shared_memory_size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The value for the size (in MiB) of the <b>/dev/shm</b> volume.</p>"""
    swappiness: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>Configures the container's memory swappiness behavior. Determines how aggressively pages are swapped. The higher the value, the more aggressive the swappiness. The default is 60.</p>"""
    tmpfs: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_list.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsList"
    ]
    """<p>The container path, mount options, and size (in MiB) of the tmpfs mount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails,
) -> dict:
    out: dict = {}
    if "capabilities" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_capabilities_details

        out["Capabilities"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_capabilities_details.serialize_json(
                value["capabilities"]
            )
        )
    if "devices" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_list

        out["Devices"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_list.serialize_json(
                value["devices"]
            )
        )
    if "init_process_enabled" in value:
        out["InitProcessEnabled"] = value["init_process_enabled"]
    if "max_swap" in value:
        out["MaxSwap"] = value["max_swap"]
    if "shared_memory_size" in value:
        out["SharedMemorySize"] = value["shared_memory_size"]
    if "swappiness" in value:
        out["Swappiness"] = value["swappiness"]
    if "tmpfs" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_list

        out["Tmpfs"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_list.serialize_json(
                value["tmpfs"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails = {}  # type: ignore[typeddict-item]
    if "Capabilities" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_capabilities_details

        out["capabilities"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_capabilities_details.deserialize_json(
                data["Capabilities"]
            )
        )
    if "Devices" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_list

        out["devices"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_devices_list.deserialize_json(
                data["Devices"]
            )
        )
    if "InitProcessEnabled" in data:
        out["init_process_enabled"] = data["InitProcessEnabled"]
    if "MaxSwap" in data:
        out["max_swap"] = data["MaxSwap"]
    if "SharedMemorySize" in data:
        out["shared_memory_size"] = data["SharedMemorySize"]
    if "Swappiness" in data:
        out["swappiness"] = data["Swappiness"]
    if "Tmpfs" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_list

        out["tmpfs"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_tmpfs_list.deserialize_json(
                data["Tmpfs"]
            )
        )
    return out
