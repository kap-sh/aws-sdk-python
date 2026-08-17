"""Generated from Smithy shape ``com.amazonaws.ecs#Volume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.docker_volume_configuration
    import capo_ecs.types.efs_volume_configuration
    import capo_ecs.types.f_sx_windows_file_server_volume_configuration
    import capo_ecs.types.host_volume_properties
    import capo_ecs.types.s3_files_volume_configuration
    import capo_ecs.types.string


class Volume(TypedDict, closed=True):
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p> <p>When using a volume configured at launch, the <code>name</code> is required and must also be specified as the volume name in the <code>ServiceVolumeConfiguration</code> or <code>TaskVolumeConfiguration</code> parameter when creating your service or standalone task.</p> <p>For all other types of volumes, this name is referenced in the <code>sourceVolume</code> parameter of the <code>mountPoints</code> object in the container definition.</p> <p>When a volume is using the <code>efsVolumeConfiguration</code>, the name is required.</p> <p>When a volume is using the <code>s3filesVolumeConfiguration</code>, the name is required.</p>"""
    host: NotRequired["capo_ecs.types.host_volume_properties.HostVolumeProperties"]
    r"""<p>This parameter is specified when you use bind mount host volumes. The contents of the <code>host</code> parameter determine whether your bind mount host volume persists on the host container instance and where it's stored. If the <code>host</code> parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.</p> <p>Windows containers can mount whole directories on the same drive as <code>$env:ProgramData</code>. Windows containers can't mount directories on a different drive, and mount point can't be across drives. For example, you can mount <code>C:\my\path:C:\my\path</code> and <code>D:\:D:\</code>, but not <code>D:\my\path:C:\my\path</code> or <code>D:\:C:\my\path</code>.</p>"""
    docker_volume_configuration: NotRequired[
        "capo_ecs.types.docker_volume_configuration.DockerVolumeConfiguration"
    ]
    """<p>This parameter is specified when you use Docker volumes.</p> <p>Windows containers only support the use of the <code>local</code> driver. To use bind mounts, specify the <code>host</code> parameter instead.</p> <note> <p>Docker volumes aren't supported by tasks run on Fargate.</p> </note>"""
    efs_volume_configuration: NotRequired[
        "capo_ecs.types.efs_volume_configuration.EFSVolumeConfiguration"
    ]
    """<p>This parameter is specified when you use an Amazon Elastic File System file system for task storage.</p>"""
    s3files_volume_configuration: NotRequired[
        "capo_ecs.types.s3_files_volume_configuration.S3FilesVolumeConfiguration"
    ]
    """<p>This parameter is specified when you use an Amazon S3 Files file system for task storage.</p>"""
    fsx_windows_file_server_volume_configuration: NotRequired[
        "capo_ecs.types.f_sx_windows_file_server_volume_configuration.FSxWindowsFileServerVolumeConfiguration"
    ]
    """<p>This parameter is specified when you use Amazon FSx for Windows File Server file system for task storage.</p>"""
    configured_at_launch: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether the volume should be configured at launch time. This is used to create Amazon EBS volumes for standalone tasks or tasks created as part of a service. Each task definition revision may only have one volume configured at launch in the volume configuration.</p> <p>To configure a volume at launch time, use this task definition revision and specify a <code>volumeConfigurations</code> object when calling the <code>CreateService</code>, <code>UpdateService</code>, <code>RunTask</code> or <code>StartTask</code> APIs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Volume) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "host" in value:
        import capo_ecs.types.host_volume_properties

        out["host"] = capo_ecs.types.host_volume_properties.serialize_aws_json_1_1(
            value["host"]
        )
    if "docker_volume_configuration" in value:
        import capo_ecs.types.docker_volume_configuration

        out["dockerVolumeConfiguration"] = (
            capo_ecs.types.docker_volume_configuration.serialize_aws_json_1_1(
                value["docker_volume_configuration"]
            )
        )
    if "efs_volume_configuration" in value:
        import capo_ecs.types.efs_volume_configuration

        out["efsVolumeConfiguration"] = (
            capo_ecs.types.efs_volume_configuration.serialize_aws_json_1_1(
                value["efs_volume_configuration"]
            )
        )
    if "s3files_volume_configuration" in value:
        import capo_ecs.types.s3_files_volume_configuration

        out["s3filesVolumeConfiguration"] = (
            capo_ecs.types.s3_files_volume_configuration.serialize_aws_json_1_1(
                value["s3files_volume_configuration"]
            )
        )
    if "fsx_windows_file_server_volume_configuration" in value:
        import capo_ecs.types.f_sx_windows_file_server_volume_configuration

        out["fsxWindowsFileServerVolumeConfiguration"] = (
            capo_ecs.types.f_sx_windows_file_server_volume_configuration.serialize_aws_json_1_1(
                value["fsx_windows_file_server_volume_configuration"]
            )
        )
    if "configured_at_launch" in value:
        out["configuredAtLaunch"] = value["configured_at_launch"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Volume:
    out: Volume = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("host") is not None:
        import capo_ecs.types.host_volume_properties

        out["host"] = capo_ecs.types.host_volume_properties.deserialize_aws_json_1_1(
            data["host"]
        )
    if data.get("dockerVolumeConfiguration") is not None:
        import capo_ecs.types.docker_volume_configuration

        out["docker_volume_configuration"] = (
            capo_ecs.types.docker_volume_configuration.deserialize_aws_json_1_1(
                data["dockerVolumeConfiguration"]
            )
        )
    if data.get("efsVolumeConfiguration") is not None:
        import capo_ecs.types.efs_volume_configuration

        out["efs_volume_configuration"] = (
            capo_ecs.types.efs_volume_configuration.deserialize_aws_json_1_1(
                data["efsVolumeConfiguration"]
            )
        )
    if data.get("s3filesVolumeConfiguration") is not None:
        import capo_ecs.types.s3_files_volume_configuration

        out["s3files_volume_configuration"] = (
            capo_ecs.types.s3_files_volume_configuration.deserialize_aws_json_1_1(
                data["s3filesVolumeConfiguration"]
            )
        )
    if data.get("fsxWindowsFileServerVolumeConfiguration") is not None:
        import capo_ecs.types.f_sx_windows_file_server_volume_configuration

        out["fsx_windows_file_server_volume_configuration"] = (
            capo_ecs.types.f_sx_windows_file_server_volume_configuration.deserialize_aws_json_1_1(
                data["fsxWindowsFileServerVolumeConfiguration"]
            )
        )
    if data.get("configuredAtLaunch") is not None:
        out["configured_at_launch"] = data["configuredAtLaunch"]
    return out
