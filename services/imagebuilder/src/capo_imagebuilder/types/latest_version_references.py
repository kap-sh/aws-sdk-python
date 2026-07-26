"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LatestVersionReferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_builder_arn


class LatestVersionReferences(TypedDict, closed=True):
    latest_version_arn: NotRequired[
        "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    ]
    """<p>The latest version Amazon Resource Name (ARN) of the Image Builder resource.</p>"""
    latest_major_version_arn: NotRequired[
        "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    ]
    """<p>The latest version Amazon Resource Name (ARN) with the same <code>major</code> version of the Image Builder resource.</p>"""
    latest_minor_version_arn: NotRequired[
        "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    ]
    """<p>The latest version Amazon Resource Name (ARN) with the same <code>minor</code> version of the Image Builder resource.</p>"""
    latest_patch_version_arn: NotRequired[
        "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    ]
    """<p>The latest version Amazon Resource Name (ARN) with the same <code>patch</code> version of the Image Builder resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LatestVersionReferences) -> dict:
    out: dict = {}
    if "latest_version_arn" in value:
        out["latestVersionArn"] = value["latest_version_arn"]
    if "latest_major_version_arn" in value:
        out["latestMajorVersionArn"] = value["latest_major_version_arn"]
    if "latest_minor_version_arn" in value:
        out["latestMinorVersionArn"] = value["latest_minor_version_arn"]
    if "latest_patch_version_arn" in value:
        out["latestPatchVersionArn"] = value["latest_patch_version_arn"]
    return out


def deserialize_json(data: dict) -> LatestVersionReferences:
    out: LatestVersionReferences = {}  # type: ignore[typeddict-item]
    if "latestVersionArn" in data:
        out["latest_version_arn"] = data["latestVersionArn"]
    if "latestMajorVersionArn" in data:
        out["latest_major_version_arn"] = data["latestMajorVersionArn"]
    if "latestMinorVersionArn" in data:
        out["latest_minor_version_arn"] = data["latestMinorVersionArn"]
    if "latestPatchVersionArn" in data:
        out["latest_patch_version_arn"] = data["latestPatchVersionArn"]
    return out
