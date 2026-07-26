"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImageRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_recipe
    import capo_imagebuilder.types.latest_version_references
    import capo_imagebuilder.types.non_empty_string


class GetImageRecipeResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_recipe: NotRequired["capo_imagebuilder.types.image_recipe.ImageRecipe"]
    """<p>The image recipe object.</p>"""
    latest_version_references: NotRequired[
        "capo_imagebuilder.types.latest_version_references.LatestVersionReferences"
    ]
    """<p>The resource ARNs with different wildcard variations of semantic versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageRecipeResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_recipe" in value:
        import capo_imagebuilder.types.image_recipe

        out["imageRecipe"] = capo_imagebuilder.types.image_recipe.serialize_json(
            value["image_recipe"]
        )
    if "latest_version_references" in value:
        import capo_imagebuilder.types.latest_version_references

        out["latestVersionReferences"] = (
            capo_imagebuilder.types.latest_version_references.serialize_json(
                value["latest_version_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetImageRecipeResponse:
    out: GetImageRecipeResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imageRecipe" in data:
        import capo_imagebuilder.types.image_recipe

        out["image_recipe"] = capo_imagebuilder.types.image_recipe.deserialize_json(
            data["imageRecipe"]
        )
    if "latestVersionReferences" in data:
        import capo_imagebuilder.types.latest_version_references

        out["latest_version_references"] = (
            capo_imagebuilder.types.latest_version_references.deserialize_json(
                data["latestVersionReferences"]
            )
        )
    return out
