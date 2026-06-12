"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageRecipeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_recipe_summary

ImageRecipeSummaryList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.image_recipe_summary.ImageRecipeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageRecipeSummaryList) -> list:
    import aws_sdk_imagebuilder.types.image_recipe_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_imagebuilder.types.image_recipe_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageRecipeSummaryList:
    import aws_sdk_imagebuilder.types.image_recipe_summary

    out: ImageRecipeSummaryList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.image_recipe_summary.deserialize_json(item)
        )
    return out
