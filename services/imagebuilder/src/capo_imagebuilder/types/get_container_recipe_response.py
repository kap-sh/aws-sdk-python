"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetContainerRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.container_recipe
    import capo_imagebuilder.types.latest_version_references
    import capo_imagebuilder.types.non_empty_string


class GetContainerRecipeResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    container_recipe: NotRequired[
        "capo_imagebuilder.types.container_recipe.ContainerRecipe"
    ]
    """<p>The container recipe object that is returned.</p>"""
    latest_version_references: NotRequired[
        "capo_imagebuilder.types.latest_version_references.LatestVersionReferences"
    ]
    """<p>The resource ARNs with different wildcard variations of semantic versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContainerRecipeResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "container_recipe" in value:
        import capo_imagebuilder.types.container_recipe

        out["containerRecipe"] = (
            capo_imagebuilder.types.container_recipe.serialize_json(
                value["container_recipe"]
            )
        )
    if "latest_version_references" in value:
        import capo_imagebuilder.types.latest_version_references

        out["latestVersionReferences"] = (
            capo_imagebuilder.types.latest_version_references.serialize_json(
                value["latest_version_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetContainerRecipeResponse:
    out: GetContainerRecipeResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "containerRecipe" in data:
        import capo_imagebuilder.types.container_recipe

        out["container_recipe"] = (
            capo_imagebuilder.types.container_recipe.deserialize_json(
                data["containerRecipe"]
            )
        )
    if "latestVersionReferences" in data:
        import capo_imagebuilder.types.latest_version_references

        out["latest_version_references"] = (
            capo_imagebuilder.types.latest_version_references.deserialize_json(
                data["latestVersionReferences"]
            )
        )
    return out
