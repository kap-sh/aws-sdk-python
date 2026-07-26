"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ContainerLogRotationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.max_files_to_keep
    import capo_emr_containers.types.rotation_size


class ContainerLogRotationConfiguration(TypedDict, closed=True):
    rotation_size: "capo_emr_containers.types.rotation_size.RotationSize"
    """<p>The file size at which to rotate logs. Minimum of 2KB, Maximum of 2GB.</p>"""
    max_files_to_keep: "capo_emr_containers.types.max_files_to_keep.MaxFilesToKeep"
    """<p>The number of files to keep in container after rotation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerLogRotationConfiguration) -> dict:
    out: dict = {}
    out["rotationSize"] = value["rotation_size"]
    out["maxFilesToKeep"] = value["max_files_to_keep"]
    return out


def deserialize_json(data: dict) -> ContainerLogRotationConfiguration:
    out: ContainerLogRotationConfiguration = {}  # type: ignore[typeddict-item]
    if "rotationSize" in data:
        out["rotation_size"] = data["rotationSize"]
    else:
        raise DeserializationError(
            "ContainerLogRotationConfiguration.rotation_size required"
        )
    if "maxFilesToKeep" in data:
        out["max_files_to_keep"] = data["maxFilesToKeep"]
    else:
        raise DeserializationError(
            "ContainerLogRotationConfiguration.max_files_to_keep required"
        )
    return out
