"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartResourceSnapshotJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier


class StartResourceSnapshotJobRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Starts the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Starts the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>"""
    resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    """<p>The identifier of the resource snapshot job to start.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartResourceSnapshotJobRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ResourceSnapshotJobIdentifier"] = value["resource_snapshot_job_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartResourceSnapshotJobRequest:
    out: StartResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("StartResourceSnapshotJobRequest.catalog required")
    if "ResourceSnapshotJobIdentifier" in data:
        out["resource_snapshot_job_identifier"] = data["ResourceSnapshotJobIdentifier"]
    else:
        raise DeserializationError(
            "StartResourceSnapshotJobRequest.resource_snapshot_job_identifier required"
        )
    return out
