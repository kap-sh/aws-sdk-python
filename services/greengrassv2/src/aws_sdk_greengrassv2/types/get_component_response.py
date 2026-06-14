"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetComponentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.recipe_blob
    import aws_sdk_greengrassv2.types.recipe_output_format
    import aws_sdk_greengrassv2.types.tag_map


class GetComponentResponse(TypedDict):
    recipe_output_format: (
        "aws_sdk_greengrassv2.types.recipe_output_format.RecipeOutputFormat"
    )
    """<p>The format of the recipe.</p>"""
    recipe: "aws_sdk_greengrassv2.types.recipe_blob.RecipeBlob"
    """<p>The recipe of the component version.</p>"""
    tags: NotRequired["aws_sdk_greengrassv2.types.tag_map.TagMap"]
    r"""<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href=\"https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html\">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentResponse) -> dict:
    out: dict = {}
    import aws_sdk_greengrassv2.types.recipe_output_format

    out["recipeOutputFormat"] = (
        aws_sdk_greengrassv2.types.recipe_output_format.serialize_json(
            value["recipe_output_format"]
        )
    )
    import aws_sdk_greengrassv2.types.recipe_blob

    out["recipe"] = aws_sdk_greengrassv2.types.recipe_blob.serialize_json(
        value["recipe"]
    )
    if "tags" in value:
        import aws_sdk_greengrassv2.types.tag_map

        out["tags"] = aws_sdk_greengrassv2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetComponentResponse:
    out: GetComponentResponse = {}  # type: ignore[typeddict-item]
    if "recipeOutputFormat" in data:
        import aws_sdk_greengrassv2.types.recipe_output_format

        out["recipe_output_format"] = (
            aws_sdk_greengrassv2.types.recipe_output_format.deserialize_json(
                data["recipeOutputFormat"]
            )
        )
    else:
        raise DeserializationError("GetComponentResponse.recipe_output_format required")
    if "recipe" in data:
        import aws_sdk_greengrassv2.types.recipe_blob

        out["recipe"] = aws_sdk_greengrassv2.types.recipe_blob.deserialize_json(
            data["recipe"]
        )
    else:
        raise DeserializationError("GetComponentResponse.recipe required")
    if "tags" in data:
        import aws_sdk_greengrassv2.types.tag_map

        out["tags"] = aws_sdk_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    return out
