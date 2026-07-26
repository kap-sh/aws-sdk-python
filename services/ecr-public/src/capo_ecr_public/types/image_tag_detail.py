"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ImageTagDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.creation_timestamp
    import capo_ecr_public.types.image_tag
    import capo_ecr_public.types.referenced_image_detail


class ImageTagDetail(TypedDict, closed=True):
    image_tag: NotRequired["capo_ecr_public.types.image_tag.ImageTag"]
    """<p>The tag that's associated with the image.</p>"""
    created_at: NotRequired[
        "capo_ecr_public.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>The time stamp that indicates when the image tag was created.</p>"""
    image_detail: NotRequired[
        "capo_ecr_public.types.referenced_image_detail.ReferencedImageDetail"
    ]
    """<p>An object that describes the details of an image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagDetail) -> dict:
    out: dict = {}
    if "image_tag" in value:
        out["imageTag"] = value["image_tag"]
    if "created_at" in value:
        import capo_ecr_public.types.creation_timestamp

        out["createdAt"] = (
            capo_ecr_public.types.creation_timestamp.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "image_detail" in value:
        import capo_ecr_public.types.referenced_image_detail

        out["imageDetail"] = (
            capo_ecr_public.types.referenced_image_detail.serialize_aws_json_1_1(
                value["image_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageTagDetail:
    out: ImageTagDetail = {}  # type: ignore[typeddict-item]
    if "imageTag" in data:
        out["image_tag"] = data["imageTag"]
    if "createdAt" in data:
        import capo_ecr_public.types.creation_timestamp

        out["created_at"] = (
            capo_ecr_public.types.creation_timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "imageDetail" in data:
        import capo_ecr_public.types.referenced_image_detail

        out["image_detail"] = (
            capo_ecr_public.types.referenced_image_detail.deserialize_aws_json_1_1(
                data["imageDetail"]
            )
        )
    return out
