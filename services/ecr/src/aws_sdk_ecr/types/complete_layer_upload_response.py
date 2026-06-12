"""Generated from Smithy shape ``com.amazonaws.ecr#CompleteLayerUploadResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.layer_digest
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.upload_id


class CompleteLayerUploadResponse(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    upload_id: NotRequired["aws_sdk_ecr.types.upload_id.UploadId"]
    """<p>The upload ID associated with the layer.</p>"""
    layer_digest: NotRequired["aws_sdk_ecr.types.layer_digest.LayerDigest"]
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
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    if "layerDigest" in data:
        out["layer_digest"] = data["layerDigest"]
    return out
