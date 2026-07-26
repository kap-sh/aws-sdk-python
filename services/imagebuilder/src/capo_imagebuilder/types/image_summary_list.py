"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_summary

ImageSummaryList: TypeAlias = list["capo_imagebuilder.types.image_summary.ImageSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSummaryList) -> list:
    import capo_imagebuilder.types.image_summary

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.image_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageSummaryList:
    import capo_imagebuilder.types.image_summary

    out: ImageSummaryList = []
    for item in data:
        out.append(capo_imagebuilder.types.image_summary.deserialize_json(item))
    return out
