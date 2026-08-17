"""Generated from Smithy shape ``com.amazonaws.ecr#CompleteLayerUploadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.layer_digest
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name
    import capo_ecr.types.upload_id


class CompleteLayerUploadResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    upload_id: NotRequired["capo_ecr.types.upload_id.UploadId"]
    """<p>The upload ID associated with the layer.</p>"""
    layer_digest: NotRequired["capo_ecr.types.layer_digest.LayerDigest"]
    """<p>The <code>sha256</code> digest of the image layer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompleteLayerUploadResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "upload_id" in value:
        out["uploadId"] = value["upload_id"]
    if "layer_digest" in value:
        out["layerDigest"] = value["layer_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CompleteLayerUploadResponse:
    out: CompleteLayerUploadResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    if data.get("layerDigest") is not None:
        out["layer_digest"] = data["layerDigest"]
    return out
