"""Generated from Smithy shape ``com.amazonaws.ecr#ImageIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_digest
    import aws_sdk_ecr.types.image_tag


class ImageIdentifier(TypedDict, closed=True):
    image_digest: NotRequired["aws_sdk_ecr.types.image_digest.ImageDigest"]
    """<p>The <code>sha256</code> digest of the image manifest.</p>"""
    image_tag: NotRequired["aws_sdk_ecr.types.image_tag.ImageTag"]
    """<p>The tag used for the image.</p>"""


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
