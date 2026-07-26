"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_firelens_configuration_details
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_health_check_details
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_details
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_details
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_repository_credentials_details
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_list
    import capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.field_map
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEcsTaskDefinitionContainerDefinitionsDetails(TypedDict, closed=True):
    command: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The command that is passed to the container.</p>"""
    cpu: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of CPU units reserved for the container.</p>"""
    depends_on: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_list.AwsEcsTaskDefinitionContainerDefinitionsDependsOnList"
    ]
    """<p>The dependencies that are defined for container startup and shutdown.</p>"""
    disable_networking: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to disable networking within the container.</p>"""
    dns_search_domains: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of DNS search domains that are presented to the container.</p>"""
    dns_servers: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of DNS servers that are presented to the container.</p>"""
    docker_labels: NotRequired["capo_securityhub.types.field_map.FieldMap"]
    """<p>A key-value map of labels to add to the container.</p>"""
    docker_security_options: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems.</p>"""
    entry_point: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The entry point that is passed to the container.</p>"""
    environment: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_list.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentList"
    ]
    """<p>The environment variables to pass to a container.</p>"""
    environment_files: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_list.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesList"
    ]
    """<p>A list of files containing the environment variables to pass to a container.</p>"""
    essential: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the container is essential. All tasks must have at least one essential container.</p>"""
    extra_hosts: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_list.AwsEcsTaskDefinitionContainerDefinitionsExtraHostsList"
    ]
    """<p>A list of hostnames and IP address mappings to append to the <b>/etc/hosts</b> file on the container.</p>"""
    firelens_configuration: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_firelens_configuration_details.AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetails"
    ]
    """<p>The FireLens configuration for the container. Specifies and configures a log router for container logs.</p>"""
    health_check: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_health_check_details.AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails"
    ]
    """<p>The container health check command and associated configuration parameters for the container.</p>"""
    hostname: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The hostname to use for the container.</p>"""
    image: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The image used to start the container.</p>"""
    interactive: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>If set to true, then containerized applications can be deployed that require <code>stdin</code> or a <code>tty</code> to be allocated.</p>"""
    links: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of links for the container in the form <code> <i>container_name</i>:<i>alias</i> </code>. Allows containers to communicate with each other without the need for port mappings.</p>"""
    linux_parameters: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_details.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails"
    ]
    """<p>Linux-specific modifications that are applied to the container, such as Linux kernel capabilities.</p>"""
    log_configuration: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_details.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails"
    ]
    """<p>The log configuration specification for the container.</p>"""
    memory: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The amount (in MiB) of memory to present to the container. If the container attempts to exceed the memory specified here, the container is shut down. The total amount of memory reserved for all containers within a task must be lower than the task memory value, if one is specified.</p>"""
    memory_reservation: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The soft limit (in MiB) of memory to reserve for the container.</p>"""
    mount_points: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_list.AwsEcsTaskDefinitionContainerDefinitionsMountPointsList"
    ]
    """<p>The mount points for the data volumes in the container.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the container.</p>"""
    port_mappings: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_list.AwsEcsTaskDefinitionContainerDefinitionsPortMappingsList"
    ]
    """<p>The list of port mappings for the container.</p>"""
    privileged: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the container is given elevated privileges on the host container instance. The elevated privileges are similar to the root user.</p>"""
    pseudo_terminal: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to allocate a TTY to the container.</p>"""
    readonly_root_filesystem: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the container is given read-only access to its root file system.</p>"""
    repository_credentials: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_repository_credentials_details.AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails"
    ]
    """<p>The private repository authentication credentials to use.</p>"""
    resource_requirements: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_list.AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsList"
    ]
    """<p>The type and amount of a resource to assign to a container. The only supported resource is a GPU.</p>"""
    secrets: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_list.AwsEcsTaskDefinitionContainerDefinitionsSecretsList"
    ]
    """<p>The secrets to pass to the container.</p>"""
    start_timeout: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of seconds to wait before giving up on resolving dependencies for a container. </p>"""
    stop_timeout: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of seconds to wait before the container is stopped if it doesn't shut down normally on its own.</p>"""
    system_controls: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_list.AwsEcsTaskDefinitionContainerDefinitionsSystemControlsList"
    ]
    """<p>A list of namespaced kernel parameters to set in the container.</p>"""
    ulimits: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_list.AwsEcsTaskDefinitionContainerDefinitionsUlimitsList"
    ]
    """<p>A list of ulimits to set in the container. </p>"""
    user: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The user to use inside the container.</p> <p>The value can use one of the following formats.</p> <ul> <li> <p> <code> <i>user</i> </code> </p> </li> <li> <p> <code> <i>user</i> </code>:<code> <i>group</i> </code> </p> </li> <li> <p> <code> <i>uid</i> </code> </p> </li> <li> <p> <code> <i>uid</i> </code>:<code> <i>gid</i> </code> </p> </li> <li> <p> <code> <i>user</i> </code>:<code> <i>gid</i> </code> </p> </li> <li> <p> <code> <i>uid</i> </code>:<code> <i>group</i> </code> </p> </li> </ul>"""
    volumes_from: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_list.AwsEcsTaskDefinitionContainerDefinitionsVolumesFromList"
    ]
    """<p>Data volumes to mount from another container.</p>"""
    working_directory: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The working directory in which to run commands inside the container.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionContainerDefinitionsDetails) -> dict:
    out: dict = {}
    if "command" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Command"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["command"]
        )
    if "cpu" in value:
        out["Cpu"] = value["cpu"]
    if "depends_on" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_list

        out["DependsOn"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_list.serialize_json(
                value["depends_on"]
            )
        )
    if "disable_networking" in value:
        out["DisableNetworking"] = value["disable_networking"]
    if "dns_search_domains" in value:
        import capo_securityhub.types.non_empty_string_list

        out["DnsSearchDomains"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["dns_search_domains"]
            )
        )
    if "dns_servers" in value:
        import capo_securityhub.types.non_empty_string_list

        out["DnsServers"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["dns_servers"]
        )
    if "docker_labels" in value:
        import capo_securityhub.types.field_map

        out["DockerLabels"] = capo_securityhub.types.field_map.serialize_json(
            value["docker_labels"]
        )
    if "docker_security_options" in value:
        import capo_securityhub.types.non_empty_string_list

        out["DockerSecurityOptions"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["docker_security_options"]
            )
        )
    if "entry_point" in value:
        import capo_securityhub.types.non_empty_string_list

        out["EntryPoint"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["entry_point"]
        )
    if "environment" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_list

        out["Environment"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_list.serialize_json(
                value["environment"]
            )
        )
    if "environment_files" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_list

        out["EnvironmentFiles"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_list.serialize_json(
                value["environment_files"]
            )
        )
    if "essential" in value:
        out["Essential"] = value["essential"]
    if "extra_hosts" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_list

        out["ExtraHosts"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_list.serialize_json(
                value["extra_hosts"]
            )
        )
    if "firelens_configuration" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_firelens_configuration_details

        out["FirelensConfiguration"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_firelens_configuration_details.serialize_json(
                value["firelens_configuration"]
            )
        )
    if "health_check" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_health_check_details

        out["HealthCheck"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_health_check_details.serialize_json(
                value["health_check"]
            )
        )
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "image" in value:
        out["Image"] = value["image"]
    if "interactive" in value:
        out["Interactive"] = value["interactive"]
    if "links" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Links"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["links"]
        )
    if "linux_parameters" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_details

        out["LinuxParameters"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_details.serialize_json(
                value["linux_parameters"]
            )
        )
    if "log_configuration" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_details

        out["LogConfiguration"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_details.serialize_json(
                value["log_configuration"]
            )
        )
    if "memory" in value:
        out["Memory"] = value["memory"]
    if "memory_reservation" in value:
        out["MemoryReservation"] = value["memory_reservation"]
    if "mount_points" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_list

        out["MountPoints"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_list.serialize_json(
                value["mount_points"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "port_mappings" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_list

        out["PortMappings"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_list.serialize_json(
                value["port_mappings"]
            )
        )
    if "privileged" in value:
        out["Privileged"] = value["privileged"]
    if "pseudo_terminal" in value:
        out["PseudoTerminal"] = value["pseudo_terminal"]
    if "readonly_root_filesystem" in value:
        out["ReadonlyRootFilesystem"] = value["readonly_root_filesystem"]
    if "repository_credentials" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_repository_credentials_details

        out["RepositoryCredentials"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_repository_credentials_details.serialize_json(
                value["repository_credentials"]
            )
        )
    if "resource_requirements" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_list

        out["ResourceRequirements"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_list.serialize_json(
                value["resource_requirements"]
            )
        )
    if "secrets" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_list

        out["Secrets"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_list.serialize_json(
                value["secrets"]
            )
        )
    if "start_timeout" in value:
        out["StartTimeout"] = value["start_timeout"]
    if "stop_timeout" in value:
        out["StopTimeout"] = value["stop_timeout"]
    if "system_controls" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_list

        out["SystemControls"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_list.serialize_json(
                value["system_controls"]
            )
        )
    if "ulimits" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_list

        out["Ulimits"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_list.serialize_json(
                value["ulimits"]
            )
        )
    if "user" in value:
        out["User"] = value["user"]
    if "volumes_from" in value:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_list

        out["VolumesFrom"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_list.serialize_json(
                value["volumes_from"]
            )
        )
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    return out


def deserialize_json(data: dict) -> AwsEcsTaskDefinitionContainerDefinitionsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsDetails = {}  # type: ignore[typeddict-item]
    if "Command" in data:
        import capo_securityhub.types.non_empty_string_list

        out["command"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Command"]
        )
    if "Cpu" in data:
        out["cpu"] = data["Cpu"]
    if "DependsOn" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_list

        out["depends_on"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_depends_on_list.deserialize_json(
                data["DependsOn"]
            )
        )
    if "DisableNetworking" in data:
        out["disable_networking"] = data["DisableNetworking"]
    if "DnsSearchDomains" in data:
        import capo_securityhub.types.non_empty_string_list

        out["dns_search_domains"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["DnsSearchDomains"]
            )
        )
    if "DnsServers" in data:
        import capo_securityhub.types.non_empty_string_list

        out["dns_servers"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["DnsServers"]
            )
        )
    if "DockerLabels" in data:
        import capo_securityhub.types.field_map

        out["docker_labels"] = capo_securityhub.types.field_map.deserialize_json(
            data["DockerLabels"]
        )
    if "DockerSecurityOptions" in data:
        import capo_securityhub.types.non_empty_string_list

        out["docker_security_options"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["DockerSecurityOptions"]
            )
        )
    if "EntryPoint" in data:
        import capo_securityhub.types.non_empty_string_list

        out["entry_point"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["EntryPoint"]
            )
        )
    if "Environment" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_list

        out["environment"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_list.deserialize_json(
                data["Environment"]
            )
        )
    if "EnvironmentFiles" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_list

        out["environment_files"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_environment_files_list.deserialize_json(
                data["EnvironmentFiles"]
            )
        )
    if "Essential" in data:
        out["essential"] = data["Essential"]
    if "ExtraHosts" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_list

        out["extra_hosts"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_extra_hosts_list.deserialize_json(
                data["ExtraHosts"]
            )
        )
    if "FirelensConfiguration" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_firelens_configuration_details

        out["firelens_configuration"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_firelens_configuration_details.deserialize_json(
                data["FirelensConfiguration"]
            )
        )
    if "HealthCheck" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_health_check_details

        out["health_check"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_health_check_details.deserialize_json(
                data["HealthCheck"]
            )
        )
    if "Hostname" in data:
        out["hostname"] = data["Hostname"]
    if "Image" in data:
        out["image"] = data["Image"]
    if "Interactive" in data:
        out["interactive"] = data["Interactive"]
    if "Links" in data:
        import capo_securityhub.types.non_empty_string_list

        out["links"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Links"]
        )
    if "LinuxParameters" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_details

        out["linux_parameters"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_linux_parameters_details.deserialize_json(
                data["LinuxParameters"]
            )
        )
    if "LogConfiguration" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_details

        out["log_configuration"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_details.deserialize_json(
                data["LogConfiguration"]
            )
        )
    if "Memory" in data:
        out["memory"] = data["Memory"]
    if "MemoryReservation" in data:
        out["memory_reservation"] = data["MemoryReservation"]
    if "MountPoints" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_list

        out["mount_points"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_mount_points_list.deserialize_json(
                data["MountPoints"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "PortMappings" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_list

        out["port_mappings"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_port_mappings_list.deserialize_json(
                data["PortMappings"]
            )
        )
    if "Privileged" in data:
        out["privileged"] = data["Privileged"]
    if "PseudoTerminal" in data:
        out["pseudo_terminal"] = data["PseudoTerminal"]
    if "ReadonlyRootFilesystem" in data:
        out["readonly_root_filesystem"] = data["ReadonlyRootFilesystem"]
    if "RepositoryCredentials" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_repository_credentials_details

        out["repository_credentials"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_repository_credentials_details.deserialize_json(
                data["RepositoryCredentials"]
            )
        )
    if "ResourceRequirements" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_list

        out["resource_requirements"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_resource_requirements_list.deserialize_json(
                data["ResourceRequirements"]
            )
        )
    if "Secrets" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_list

        out["secrets"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_secrets_list.deserialize_json(
                data["Secrets"]
            )
        )
    if "StartTimeout" in data:
        out["start_timeout"] = data["StartTimeout"]
    if "StopTimeout" in data:
        out["stop_timeout"] = data["StopTimeout"]
    if "SystemControls" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_list

        out["system_controls"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_system_controls_list.deserialize_json(
                data["SystemControls"]
            )
        )
    if "Ulimits" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_list

        out["ulimits"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_ulimits_list.deserialize_json(
                data["Ulimits"]
            )
        )
    if "User" in data:
        out["user"] = data["User"]
    if "VolumesFrom" in data:
        import capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_list

        out["volumes_from"] = (
            capo_securityhub.types.aws_ecs_task_definition_container_definitions_volumes_from_list.deserialize_json(
                data["VolumesFrom"]
            )
        )
    if "WorkingDirectory" in data:
        out["working_directory"] = data["WorkingDirectory"]
    return out
