"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerRecipeSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.container_recipe_summary

ContainerRecipeSummaryList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.container_recipe_summary.ContainerRecipeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRecipeSummaryList) -> list:
    import aws_sdk_imagebuilder.types.container_recipe_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.container_recipe_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContainerRecipeSummaryList:
    import aws_sdk_imagebuilder.types.container_recipe_summary

    out: ContainerRecipeSummaryList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.container_recipe_summary.deserialize_json(item)
        )
    return out
