"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image
    import capo_imagebuilder.types.latest_version_references
    import capo_imagebuilder.types.non_empty_string


class GetImageResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image: NotRequired["capo_imagebuilder.types.image.Image"]
    """<p>The image object.</p>"""
    latest_version_references: NotRequired[
        "capo_imagebuilder.types.latest_version_references.LatestVersionReferences"
    ]
    """<p>The resource ARNs with different wildcard variations of semantic versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image" in value:
        import capo_imagebuilder.types.image

        out["image"] = capo_imagebuilder.types.image.serialize_json(value["image"])
    if "latest_version_references" in value:
        import capo_imagebuilder.types.latest_version_references

        out["latestVersionReferences"] = (
            capo_imagebuilder.types.latest_version_references.serialize_json(
                value["latest_version_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetImageResponse:
    out: GetImageResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "image" in data:
        import capo_imagebuilder.types.image

        out["image"] = capo_imagebuilder.types.image.deserialize_json(data["image"])
    if "latestVersionReferences" in data:
        import capo_imagebuilder.types.latest_version_references

        out["latest_version_references"] = (
            capo_imagebuilder.types.latest_version_references.deserialize_json(
                data["latestVersionReferences"]
            )
        )
    return out
