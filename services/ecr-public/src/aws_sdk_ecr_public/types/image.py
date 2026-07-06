"""Generated from Smithy shape ``com.amazonaws.ecrpublic#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.image_identifier
    import aws_sdk_ecr_public.types.image_manifest
    import aws_sdk_ecr_public.types.media_type
    import aws_sdk_ecr_public.types.registry_id_or_alias
    import aws_sdk_ecr_public.types.repository_name


class Image(TypedDict, closed=True):
    registry_id: NotRequired[
        "aws_sdk_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
    ]
    """<p>The Amazon Web Services account ID that's associated with the registry containing the image.</p>"""
    repository_name: NotRequired[
        "aws_sdk_ecr_public.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository that's associated with the image.</p>"""
    image_id: NotRequired["aws_sdk_ecr_public.types.image_identifier.ImageIdentifier"]
    """<p>An object that contains the image tag and image digest associated with an image.</p>"""
    image_manifest: NotRequired["aws_sdk_ecr_public.types.image_manifest.ImageManifest"]
    """<p>The image manifest that's associated with the image.</p>"""
    image_manifest_media_type: NotRequired[
        "aws_sdk_ecr_public.types.media_type.MediaType"
    ]
    """<p>The manifest media type of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Image) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_id" in value:
        import aws_sdk_ecr_public.types.image_identifier

        out["imageId"] = (
            aws_sdk_ecr_public.types.image_identifier.serialize_aws_json_1_1(
                value["image_id"]
            )
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
        import aws_sdk_ecr_public.types.image_identifier

        out["image_id"] = (
            aws_sdk_ecr_public.types.image_identifier.deserialize_aws_json_1_1(
                data["imageId"]
            )
        )
    if "imageManifest" in data:
        out["image_manifest"] = data["imageManifest"]
    if "imageManifestMediaType" in data:
        out["image_manifest_media_type"] = data["imageManifestMediaType"]
    return out
