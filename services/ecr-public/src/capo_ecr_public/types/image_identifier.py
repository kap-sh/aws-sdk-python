"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ImageIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.image_digest
    import capo_ecr_public.types.image_tag


class ImageIdentifier(TypedDict, closed=True):
    image_digest: NotRequired["capo_ecr_public.types.image_digest.ImageDigest"]
    """<p>The <code>sha256</code> digest of the image manifest.</p>"""
    image_tag: NotRequired["capo_ecr_public.types.image_tag.ImageTag"]
    """<p>The tag that's used for the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageIdentifier) -> dict:
    out: dict = {}
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "image_tag" in value:
        out["imageTag"] = value["image_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageIdentifier:
    out: ImageIdentifier = {}  # type: ignore[typeddict-item]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    if "imageTag" in data:
        out["image_tag"] = data["imageTag"]
    return out
