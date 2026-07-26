"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#DeleteResourceSnapshotJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_identifier


class DeleteResourceSnapshotJobRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog from which to delete the snapshot job. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>"""
    resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    """<p> The unique identifier of the resource snapshot job to be deleted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteResourceSnapshotJobRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ResourceSnapshotJobIdentifier"] = value["resource_snapshot_job_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteResourceSnapshotJobRequest:
    out: DeleteResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("DeleteResourceSnapshotJobRequest.catalog required")
    if "ResourceSnapshotJobIdentifier" in data:
        out["resource_snapshot_job_identifier"] = data["ResourceSnapshotJobIdentifier"]
    else:
        raise DeserializationError(
            "DeleteResourceSnapshotJobRequest.resource_snapshot_job_identifier required"
        )
    return out
