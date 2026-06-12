"""Generated from Smithy shape ``com.amazonaws.ecr#GetDownloadUrlForLayerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.layer_digest
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class GetDownloadUrlForLayerRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that is associated with the image layer to download.</p>"""
    layer_digest: "aws_sdk_ecr.types.layer_digest.LayerDigest"
    """<p>The digest of the image layer to download.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDownloadUrlForLayerRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["layerDigest"] = value["layer_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDownloadUrlForLayerRequest:
    out: GetDownloadUrlForLayerRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "GetDownloadUrlForLayerRequest.repository_name required"
        )
    if "layerDigest" in data:
        out["layer_digest"] = data["layerDigest"]
    else:
        raise DeserializationError(
            "GetDownloadUrlForLayerRequest.layer_digest required"
        )
    return out
