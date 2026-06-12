"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ReferencedImageDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.image_digest
    import aws_sdk_ecr_public.types.image_size_in_bytes
    import aws_sdk_ecr_public.types.media_type
    import aws_sdk_ecr_public.types.push_timestamp


class ReferencedImageDetail(TypedDict):
    image_digest: NotRequired["aws_sdk_ecr_public.types.image_digest.ImageDigest"]
    """<p>The <code>sha256</code> digest of the image manifest.</p>"""
    image_size_in_bytes: NotRequired[
        "aws_sdk_ecr_public.types.image_size_in_bytes.ImageSizeInBytes"
    ]
    """<p>The size, in bytes, of the image in the repository.</p> <p>If the image is a manifest list, this is the max size of all manifests in the list.</p> <note> <p>Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the <code>docker images</code> command shows the uncompressed image size, so it might return a larger image size than the image sizes that are returned by <a>DescribeImages</a>.</p> </note>"""
    image_pushed_at: NotRequired[
        "aws_sdk_ecr_public.types.push_timestamp.PushTimestamp"
    ]
    """<p>The date and time, expressed in standard JavaScript date format, which the current image tag was pushed to the repository at.</p>"""
    image_manifest_media_type: NotRequired[
        "aws_sdk_ecr_public.types.media_type.MediaType"
    ]
    """<p>The media type of the image manifest.</p>"""
    artifact_media_type: NotRequired["aws_sdk_ecr_public.types.media_type.MediaType"]
    """<p>The artifact media type of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferencedImageDetail) -> dict:
    out: dict = {}
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "image_size_in_bytes" in value:
        out["imageSizeInBytes"] = value["image_size_in_bytes"]
    if "image_pushed_at" in value:
        import aws_sdk_ecr_public.types.push_timestamp

        out["imagePushedAt"] = (
            aws_sdk_ecr_public.types.push_timestamp.serialize_aws_json_1_1(
                value["image_pushed_at"]
            )
        )
    if "image_manifest_media_type" in value:
        out["imageManifestMediaType"] = value["image_manifest_media_type"]
    if "artifact_media_type" in value:
        out["artifactMediaType"] = value["artifact_media_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferencedImageDetail:
    out: ReferencedImageDetail = {}  # type: ignore[typeddict-item]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    if "imageSizeInBytes" in data:
        out["image_size_in_bytes"] = data["imageSizeInBytes"]
    if "imagePushedAt" in data:
        import aws_sdk_ecr_public.types.push_timestamp

        out["image_pushed_at"] = (
            aws_sdk_ecr_public.types.push_timestamp.deserialize_aws_json_1_1(
                data["imagePushedAt"]
            )
        )
    if "imageManifestMediaType" in data:
        out["image_manifest_media_type"] = data["imageManifestMediaType"]
    if "artifactMediaType" in data:
        out["artifact_media_type"] = data["artifactMediaType"]
    return out
