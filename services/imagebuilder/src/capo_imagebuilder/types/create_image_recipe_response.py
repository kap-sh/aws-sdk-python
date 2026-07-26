"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateImageRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.image_recipe_arn
    import capo_imagebuilder.types.latest_version_references
    import capo_imagebuilder.types.non_empty_string


class CreateImageRecipeResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    client_token: NotRequired["capo_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""
    image_recipe_arn: NotRequired[
        "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image recipe that was created by this request.</p>"""
    latest_version_references: NotRequired[
        "capo_imagebuilder.types.latest_version_references.LatestVersionReferences"
    ]
    """<p>The resource ARNs with different wildcard variations of semantic versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImageRecipeResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "image_recipe_arn" in value:
        out["imageRecipeArn"] = value["image_recipe_arn"]
    if "latest_version_references" in value:
        import capo_imagebuilder.types.latest_version_references

        out["latestVersionReferences"] = (
            capo_imagebuilder.types.latest_version_references.serialize_json(
                value["latest_version_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateImageRecipeResponse:
    out: CreateImageRecipeResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "imageRecipeArn" in data:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    if "latestVersionReferences" in data:
        import capo_imagebuilder.types.latest_version_references

        out["latest_version_references"] = (
            capo_imagebuilder.types.latest_version_references.deserialize_json(
                data["latestVersionReferences"]
            )
        )
    return out
