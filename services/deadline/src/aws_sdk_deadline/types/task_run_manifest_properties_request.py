"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunManifestPropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.string


class TaskRunManifestPropertiesRequest(TypedDict):
    output_manifest_path: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>The manifest file path.</p>"""
    output_manifest_hash: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>The hash value of the file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunManifestPropertiesRequest) -> dict:
    out: dict = {}
    if "output_manifest_path" in value:
        out["outputManifestPath"] = value["output_manifest_path"]
    if "output_manifest_hash" in value:
        out["outputManifestHash"] = value["output_manifest_hash"]
    return out


def deserialize_json(data: dict) -> TaskRunManifestPropertiesRequest:
    out: TaskRunManifestPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "outputManifestPath" in data:
        out["output_manifest_path"] = data["outputManifestPath"]
    if "outputManifestHash" in data:
        out["output_manifest_hash"] = data["outputManifestHash"]
    return out
