"""Generated from Smithy shape ``com.amazonaws.ecs#HostVolumeProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class HostVolumeProperties(TypedDict, closed=True):
    source_path: NotRequired["capo_ecs.types.string.String"]
    """<p>When the <code>host</code> parameter is used, specify a <code>sourcePath</code> to declare the path on the host container instance that's presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the <code>host</code> parameter contains a <code>sourcePath</code> file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the <code>sourcePath</code> value doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.</p> <p>If you're using the Fargate launch type, the <code>sourcePath</code> parameter is not supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostVolumeProperties) -> dict:
    out: dict = {}
    if "source_path" in value:
        out["sourcePath"] = value["source_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HostVolumeProperties:
    out: HostVolumeProperties = {}  # type: ignore[typeddict-item]
    if "sourcePath" in data:
        out["source_path"] = data["sourcePath"]
    return out
