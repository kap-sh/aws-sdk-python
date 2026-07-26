"""Generated from Smithy shape ``com.amazonaws.ecr#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier
    import capo_ecr.types.image_manifest
    import capo_ecr.types.media_type
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class Image(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry containing the image.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository associated with the image.</p>"""
    image_id: NotRequired["capo_ecr.types.image_identifier.ImageIdentifier"]
    """<p>An object containing the image tag and image digest associated with an image.</p>"""
    image_manifest: NotRequired["capo_ecr.types.image_manifest.ImageManifest"]
    """<p>The image manifest associated with the image.</p>"""
    image_manifest_media_type: NotRequired["capo_ecr.types.media_type.MediaType"]
    """<p>The manifest media type of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Image) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_id" in value:
        import capo_ecr.types.image_identifier

        out["imageId"] = capo_ecr.types.image_identifier.serialize_aws_json_1_1(
            value["image_id"]
        )
    if "image_manifest" in value:
        out["imageManifest"] = value["image_manifest"]
    if "image_manifest_media_type" in value:
        out["imageManifestMediaType"] = value["image_manifest_media_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "imageId" in data:
        import capo_ecr.types.image_identifier

        out["image_id"] = capo_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    if "imageManifest" in data:
        out["image_manifest"] = data["imageManifest"]
    if "imageManifestMediaType" in data:
        out["image_manifest_media_type"] = data["imageManifestMediaType"]
    return out
