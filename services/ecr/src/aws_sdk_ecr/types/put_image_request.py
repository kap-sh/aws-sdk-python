"""Generated from Smithy shape ``com.amazonaws.ecr#PutImageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_digest
    import aws_sdk_ecr.types.image_manifest
    import aws_sdk_ecr.types.image_tag
    import aws_sdk_ecr.types.media_type
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class PutImageRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository in which to put the image.</p>"""
    image_manifest: "aws_sdk_ecr.types.image_manifest.ImageManifest"
    """<p>The image manifest corresponding to the image to be uploaded.</p>"""
    image_manifest_media_type: NotRequired["aws_sdk_ecr.types.media_type.MediaType"]
    """<p>The media type of the image manifest. If you push an image manifest that does not contain the <code>mediaType</code> field, you must specify the <code>imageManifestMediaType</code> in the request.</p>"""
    image_tag: NotRequired["aws_sdk_ecr.types.image_tag.ImageTag"]
    """<p>The tag to associate with the image. This parameter is optional.</p>"""
    image_digest: NotRequired["aws_sdk_ecr.types.image_digest.ImageDigest"]
    """<p>The image digest of the image manifest corresponding to the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutImageRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["imageManifest"] = value["image_manifest"]
    if "image_manifest_media_type" in value:
        out["imageManifestMediaType"] = value["image_manifest_media_type"]
    if "image_tag" in value:
        out["imageTag"] = value["image_tag"]
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutImageRequest:
    out: PutImageRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("PutImageRequest.repository_name required")
    if "imageManifest" in data:
        out["image_manifest"] = data["imageManifest"]
    else:
        raise DeserializationError("PutImageRequest.image_manifest required")
    if "imageManifestMediaType" in data:
        out["image_manifest_media_type"] = data["imageManifestMediaType"]
    if "imageTag" in data:
        out["image_tag"] = data["imageTag"]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    return out
