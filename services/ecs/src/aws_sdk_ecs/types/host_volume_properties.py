"""Generated from Smithy shape ``com.amazonaws.ecs#HostVolumeProperties``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class HostVolumeProperties(TypedDict):
    source_path: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>When the <code>host</code> parameter is used, specify a <code>sourcePath</code> to declare the path on the host container instance that's presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the <code>host</code> parameter contains a <code>sourcePath</code> file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the <code>sourcePath</code> value doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.</p> <p>If you're using the Fargate launch type, the <code>sourcePath</code> parameter is not supported.</p>"""
