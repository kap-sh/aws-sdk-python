"""Generated from Smithy shape ``com.amazonaws.batch#Host``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class Host(TypedDict, closed=True):
    source_path: NotRequired["capo_batch.types.string.String"]
    """<p>The path on the host container instance that's presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location doesn't exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.</p> <note> <p>This parameter isn't applicable to jobs that run on Fargate resources. Don't provide this for these jobs.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: Host) -> dict:
    out: dict = {}
    if "source_path" in value:
        out["sourcePath"] = value["source_path"]
    return out


def deserialize_json(data: dict) -> Host:
    out: Host = {}  # type: ignore[typeddict-item]
    if "sourcePath" in data:
        out["source_path"] = data["sourcePath"]
    return out
