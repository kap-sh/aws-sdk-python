"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails(
    TypedDict, closed=True
):
    container_path: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The path on the container to mount the host volume at.</p>"""
    read_only: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the container has read-only access to the volume.</p>"""
    source_volume: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the volume to mount. Must match the name of a volume listed in <code>VolumeDetails</code> for the task definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails,
) -> dict:
    out: dict = {}
    if "container_path" in value:
        out["ContainerPath"] = value["container_path"]
    if "read_only" in value:
        out["ReadOnly"] = value["read_only"]
    if "source_volume" in value:
        out["SourceVolume"] = value["source_volume"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails = {}  # type: ignore[typeddict-item]
    if "ContainerPath" in data:
        out["container_path"] = data["ContainerPath"]
    if "ReadOnly" in data:
        out["read_only"] = data["ReadOnly"]
    if "SourceVolume" in data:
        out["source_volume"] = data["SourceVolume"]
    return out
