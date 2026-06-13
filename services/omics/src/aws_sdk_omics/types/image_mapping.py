"""Generated from Smithy shape ``com.amazonaws.omics#ImageMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.uri


class ImageMapping(TypedDict):
    source_image: NotRequired["aws_sdk_omics.types.uri.Uri"]
    """<p>Specifies the URI of the source image in the upstream registry.</p>"""
    destination_image: NotRequired["aws_sdk_omics.types.uri.Uri"]
    """<p>Specifies the URI of the corresponding image in the private ECR registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageMapping) -> dict:
    out: dict = {}
    if "source_image" in value:
        out["sourceImage"] = value["source_image"]
    if "destination_image" in value:
        out["destinationImage"] = value["destination_image"]
    return out


def deserialize_json(data: dict) -> ImageMapping:
    out: ImageMapping = {}  # type: ignore[typeddict-item]
    if "sourceImage" in data:
        out["source_image"] = data["sourceImage"]
    if "destinationImage" in data:
        out["destination_image"] = data["destinationImage"]
    return out
