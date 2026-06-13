"""Generated from Smithy shape ``com.amazonaws.omics#ImageDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.task_image_digest
    import aws_sdk_omics.types.uri


class ImageDetails(TypedDict):
    image: NotRequired["aws_sdk_omics.types.uri.Uri"]
    """<p>The URI of the container image.</p>"""
    image_digest: NotRequired["aws_sdk_omics.types.task_image_digest.TaskImageDigest"]
    """<p>The container image digest. If the image URI was transformed, this will be the digest of the container image referenced by the transformed URI.</p>"""
    source_image: NotRequired["aws_sdk_omics.types.uri.Uri"]
    """<p>URI of the source registry. If the URI is from a third-party registry, Amazon Web Services HealthOmics transforms the URI to the corresponding ECR path, using the pull-through cache mapping rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageDetails) -> dict:
    out: dict = {}
    if "image" in value:
        out["image"] = value["image"]
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "source_image" in value:
        out["sourceImage"] = value["source_image"]
    return out


def deserialize_json(data: dict) -> ImageDetails:
    out: ImageDetails = {}  # type: ignore[typeddict-item]
    if "image" in data:
        out["image"] = data["image"]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    if "sourceImage" in data:
        out["source_image"] = data["sourceImage"]
    return out
