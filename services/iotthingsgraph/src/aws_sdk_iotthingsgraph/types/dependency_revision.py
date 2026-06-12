"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DependencyRevision``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.urn
    import aws_sdk_iotthingsgraph.types.version


class DependencyRevision(TypedDict):
    id: NotRequired["aws_sdk_iotthingsgraph.types.urn.Urn"]
    """<p>The ID of the workflow or system.</p>"""
    revision_number: NotRequired["aws_sdk_iotthingsgraph.types.version.Version"]
    """<p>The revision number of the workflow or system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependencyRevision) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "revision_number" in value:
        out["revisionNumber"] = value["revision_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DependencyRevision:
    out: DependencyRevision = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "revisionNumber" in data:
        out["revision_number"] = data["revisionNumber"]
    return out
